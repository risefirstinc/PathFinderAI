# API Response Examples

## RoadMap Endpoints

### POST /careers/roadmaps - Create Roadmap
**Request:**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "milestone": "Learn Python",
  "milestone_description": "Master Python fundamentals and syntax",
  "priority": 1
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "milestone": "Learn Python",
  "milestone_description": "Master Python fundamentals and syntax",
  "priority": 1
}
```

---

### GET /careers/roadmaps - Get All Roadmaps
**Request:** `GET /careers/roadmaps?skip=0&limit=10`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "career_name": "Software Engineer",
    "milestone": "Learn Python",
    "milestone_description": "Master Python fundamentals and syntax",
    "priority": 1
  },
  {
    "id": 2,
    "career_name": "Data Scientist",
    "milestone": "Learn SQL",
    "milestone_description": "Master SQL queries and databases",
    "priority": 2
  }
]
```

---

### GET /careers/roadmaps/{id} - Get Specific Roadmap
**Request:** `GET /careers/roadmaps/1`

**Response (200 OK):**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "milestone": "Learn Python",
  "milestone_description": "Master Python fundamentals and syntax",
  "priority": 1
}
```

**Response (404 Not Found):**
```json
{
  "detail": "RoadMap not found"
}
```

---

### PUT /careers/roadmaps/{id} - Update Roadmap
**Request:**
```json
{
  "id": 1,
  "career_name": "Senior Software Engineer",
  "milestone": "Learn Advanced Python",
  "milestone_description": "Master advanced Python patterns and best practices",
  "priority": 2
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "career_name": "Senior Software Engineer",
  "milestone": "Learn Advanced Python",
  "milestone_description": "Master advanced Python patterns and best practices",
  "priority": 2
}
```

---

### DELETE /careers/roadmaps/{id} - Delete Roadmap
**Request:** `DELETE /careers/roadmaps/1`

**Response (204 No Content):**
```
(empty response body)
```

---

## Overview Endpoints

### POST /careers/overviews - Create Overview
**Request:**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "avg_salary_range": "$100,000 - $150,000",
  "avg_min_degree": "Bachelor's in Computer Science",
  "avg_time_to_complete": "4 years",
  "education_cost": "$20,000 - $100,000",
  "alternate_career_names": "Developer, Programmer"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "avg_salary_range": "$100,000 - $150,000",
  "avg_min_degree": "Bachelor's in Computer Science",
  "avg_time_to_complete": "4 years",
  "education_cost": "$20,000 - $100,000",
  "alternate_career_names": "Developer, Programmer"
}
```

---

### GET /careers/overviews - Get All Overviews
**Request:** `GET /careers/overviews?skip=0&limit=10`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "career_name": "Software Engineer",
    "avg_salary_range": "$100,000 - $150,000",
    "avg_min_degree": "Bachelor's in Computer Science",
    "avg_time_to_complete": "4 years",
    "education_cost": "$20,000 - $100,000",
    "alternate_career_names": "Developer, Programmer"
  }
]
```

---

## Location Endpoints

### POST /careers/locations - Create Location
**Request:**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "location": "San Francisco, CA"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "career_name": "Software Engineer",
  "location": "San Francisco, CA"
}
```

---

### GET /careers/locations - Get All Locations
**Request:** `GET /careers/locations?skip=0&limit=10`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "career_name": "Software Engineer",
    "location": "San Francisco, CA"
  },
  {
    "id": 2,
    "career_name": "Software Engineer",
    "location": "New York, NY"
  },
  {
    "id": 3,
    "career_name": "Data Scientist",
    "location": "Seattle, WA"
  }
]
```

---

## Error Responses

### 404 Not Found
```json
{
  "detail": "RoadMap not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "career_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Response Status Codes

| Code | Description | Example |
|------|-------------|---------|
| 200 | OK | GET, PUT successful |
| 201 | Created | POST successful |
| 204 | No Content | DELETE successful |
| 404 | Not Found | Resource doesn't exist |
| 422 | Validation Error | Invalid request data |
| 500 | Server Error | Database connection failed |

---

## Pagination Example

### Request with Pagination
```
GET /careers/roadmaps?skip=0&limit=5
```

This returns the first 5 roadmaps.

```
GET /careers/roadmaps?skip=5&limit=5
```

This returns roadmaps 6-10 (next page).

---

## Headers

### Request Headers
```
Content-Type: application/json
```

### Response Headers
```
Content-Type: application/json
```

---

## Full Workflow Example

1. **Create a Roadmap**
```bash
curl -X POST "http://localhost:8000/careers/roadmaps" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "career_name": "SWE", "milestone": "Python", "milestone_description": "Learn", "priority": 1}'
```
Response: 201 Created

2. **Get the Roadmap**
```bash
curl "http://localhost:8000/careers/roadmaps/1"
```
Response: 200 OK with roadmap data

3. **Update the Roadmap**
```bash
curl -X PUT "http://localhost:8000/careers/roadmaps/1" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "career_name": "SWE", "milestone": "Advanced Python", "milestone_description": "Master", "priority": 2}'
```
Response: 200 OK with updated data

4. **Delete the Roadmap**
```bash
curl -X DELETE "http://localhost:8000/careers/roadmaps/1"
```
Response: 204 No Content

---

**Note:** All examples use JSON format. Adjust IDs and values based on your data.
