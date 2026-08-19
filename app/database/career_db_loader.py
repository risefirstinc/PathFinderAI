"""
career_db_loader.py

Streamlines loading career data into the `career_info_db` MySQL database,
which has three related tables:

    location  (id, career_name, location)
    overview  (id, career_name, avg_salary_range, avg_min_degree,
               avg_time_to_complete, education_cost, alternate_career_names)
    roadmaps  (id, career_name, milestone, milestone_description, priority)

Instead of writing individual INSERT statements by hand in MySQL Workbench,
define your careers as Python dictionaries (or a JSON file) and run this
script. It handles:

    - One overview row per career
    - Multiple location rows per career (a career can have several locations)
    - Multiple roadmap rows per career (a career can have several milestones)
    - Transactions (all-or-nothing per career, with rollback on error)
    - Optional "refresh" mode that clears out a career's existing rows
      before re-inserting (handy when you're iterating on the data)

Requirements:
    pip install mysql-connector-python

Usage:
    1. Fill in DB_CONFIG below (or set environment variables).
    2. Either edit the SAMPLE_CAREERS list at the bottom, or point
       load_from_json() at your own JSON file (see career_data_example.json
       format described in the docstring of load_careers_from_json).
    3. Run:  python career_db_loader.py
"""

import os
import json
import mysql.connector
from mysql.connector import Error


# ---------------------------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------------------------
# Fill these in directly, or set them as environment variables and leave
# the os.environ.get() defaults in place.

# call our Settings(BaseSettings) instead of the code below
DB_CONFIG = {
    "host": os.environ.get("CAREER_DB_HOST", "localhost"),
    "user": os.environ.get("CAREER_DB_USER", "root"),
    "password": os.environ.get("CAREER_DB_PASSWORD", ""),
    "database": os.environ.get("CAREER_DB_NAME", "career_info_db"),
}


# ---------------------------------------------------------------------------
# 2. CONNECTION HELPER
# ---------------------------------------------------------------------------
# we already have a function for this, so call our existing one
def get_connection():
    """Open a connection to career_info_db."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        raise RuntimeError(f"Could not connect to the database: {e}")


# ---------------------------------------------------------------------------
# 3. PER-TABLE INSERT HELPERS
# ---------------------------------------------------------------------------

def insert_overview(cursor, career):
    """Insert the single overview row for a career."""
    sql = """
        INSERT INTO overview
            (career_name, avg_salary_range, avg_min_degree,
             avg_time_to_complete, education_cost, alternate_career_names)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        career["career_name"],
        career.get("avg_salary_range"),
        career.get("avg_min_degree"),
        career.get("avg_time_to_complete"),
        career.get("education_cost"),
        career.get("alternate_career_names"),
    )
    cursor.execute(sql, values)


def insert_locations(cursor, career):
    """Insert one or more location rows for a career.

    career["location"] can be a single string or a list of strings.
    """
    locations = career.get("location", [])
    if isinstance(locations, str):
        locations = [locations]
    if not locations:
        return

    sql = "INSERT INTO location (career_name, location) VALUES (%s, %s)"
    values = [(career["career_name"], loc) for loc in locations]
    cursor.executemany(sql, values)


def insert_roadmaps(cursor, career):
    """Insert one or more roadmap milestone rows for a career.

    career["roadmaps"] is a list of dicts:
        {"milestone": ..., "milestone_description": ..., "priority": ...}
    """
    roadmap_steps = career.get("roadmaps", [])
    if not roadmap_steps:
        return

    sql = """
        INSERT INTO roadmaps
            (career_name, milestone, milestone_description, priority)
        VALUES (%s, %s, %s, %s)
    """
    values = [
        (
            career["career_name"],
            step.get("milestone"),
            step.get("milestone_description"),
            step.get("priority"),
        )
        for step in roadmap_steps
    ]
    cursor.executemany(sql, values)


def delete_existing_career(cursor, career_name):
    """Delete any existing rows for this career across all three tables.

    Useful if you're re-running the script while iterating on your data
    and don't want duplicate rows piling up.
    """
    for table in ("overview", "location", "roadmaps"):
        cursor.execute(f"DELETE FROM {table} WHERE career_name = %s", (career_name,))


# ---------------------------------------------------------------------------
# 4. ORCHESTRATION
# ---------------------------------------------------------------------------

def load_career(conn, career, refresh=False):
    """Insert one career's full record (overview + locations + roadmaps).

    Wrapped in a transaction: if anything fails, nothing for this career
    is committed.
    """
    cursor = conn.cursor()
    try:
        if refresh:
            delete_existing_career(cursor, career["career_name"])

        insert_overview(cursor, career)
        insert_locations(cursor, career)
        insert_roadmaps(cursor, career)

        conn.commit()
        print(f"  Loaded: {career['career_name']}")
    except Error as e:
        conn.rollback()
        print(f"  FAILED: {career.get('career_name', '?')} -> {e}")
    finally:
        cursor.close()


def load_careers(careers, refresh=False):
    """Load a list of career dicts into the database."""
    conn = get_connection()
    print(f"Connected to {DB_CONFIG['database']}. Loading {len(careers)} career(s)...")
    try:
        for career in careers:
            load_career(conn, career, refresh=refresh)
    finally:
        conn.close()
    print("Done.")


def load_careers_from_json(filepath, refresh=False):
    """Load careers from a JSON file containing a list of career objects.

    Expected JSON structure:
    [
        {
            "career_name": "Software Engineer",
            "location": ["Remote", "San Francisco, CA"],
            "avg_salary_range": "$70,000 - $150,000",
            "avg_min_degree": "Bachelor's",
            "avg_time_to_complete": "4 years",
            "education_cost": "$40,000",
            "alternate_career_names": "Developer, Programmer",
            "roadmaps": [
                {
                    "milestone": "Learn programming fundamentals",
                    "milestone_description": "Pick a language and build small projects",
                    "priority": 1
                },
                {
                    "milestone": "Build a portfolio",
                    "milestone_description": "3-5 projects on GitHub",
                    "priority": 2
                }
            ]
        }
    ]
    """
    with open(filepath, "r") as f:
        careers = json.load(f)
    load_careers(careers, refresh=refresh)


# ---------------------------------------------------------------------------
# 5. EXAMPLE USAGE
# ---------------------------------------------------------------------------

SAMPLE_CAREERS = [
    {
        "career_name": "Software Engineer",
        "location": ["Remote", "San Francisco, CA", "Austin, TX"],
        "avg_salary_range": "$70,000 - $150,000",
        "avg_min_degree": "Bachelor's",
        "avg_time_to_complete": "4 years",
        "education_cost": "$40,000",
        "alternate_career_names": "Developer, Programmer",
        "roadmaps": [
            {
                "milestone": "Learn programming fundamentals",
                "milestone_description": "Pick a language (e.g. Python) and build small projects",
                "priority": 1,
            },
            {
                "milestone": "Build a portfolio",
                "milestone_description": "3-5 projects on GitHub demonstrating range",
                "priority": 2,
            },
        ],
    },
    {
        "career_name": "Registered Nurse",
        "location": ["Hospitals nationwide", "Outpatient clinics"],
        "avg_salary_range": "$60,000 - $95,000",
        "avg_min_degree": "Associate's or Bachelor's (BSN)",
        "avg_time_to_complete": "2-4 years",
        "education_cost": "$20,000 - $80,000",
        "alternate_career_names": "RN",
        "roadmaps": [
            {
                "milestone": "Complete nursing program",
                "milestone_description": "ADN or BSN from an accredited school",
                "priority": 1,
            },
            {
                "milestone": "Pass the NCLEX-RN exam",
                "milestone_description": "Required licensing exam",
                "priority": 2,
            },
        ],
    },
]


if __name__ == "__main__":
    # Option A: load the sample data defined above
    load_careers(SAMPLE_CAREERS, refresh=True)

    # Option B: load from a JSON file instead, e.g.:
    # load_careers_from_json("career_data.json", refresh=True)
