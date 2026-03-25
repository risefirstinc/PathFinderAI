# PathFinder API - AWS RDS Integration

A FastAPI application with full CRUD operations integrated with AWS RDS MySQL database.

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- AWS RDS MySQL instance
- pip or conda

### 2. Environment Configuration

Create a `.env` file in the project root with your AWS RDS credentials:

```env
# AWS RDS Configuration
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=3306
DB_USER=admin
DB_PASSWORD=your_secure_password
DB_NAME=pathfinder_db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False
```

**Note:** Replace the placeholder values with your actual AWS RDS credentials.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

Create all required tables in your AWS RDS database:

```bash
python init_db.py
```

This will create the following tables:
- `roadmaps` - Career roadmap milestones
- `overviews` - Career overview information
- `locations` - Career location data

### 5. Run the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, access the interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Available Endpoints

### RoadMap Endpoints

- `GET /careers/roadmaps` - Get all roadmaps (with pagination)
- `GET /careers/roadmaps/{id}` - Get a specific roadmap
- `POST /careers/roadmaps` - Create a new roadmap
- `PUT /careers/roadmaps/{id}` - Update a roadmap
- `DELETE /careers/roadmaps/{id}` - Delete a roadmap

### Overview Endpoints

- `GET /careers/overviews` - Get all overviews (with pagination)
- `GET /careers/overviews/{id}` - Get a specific overview
- `POST /careers/overviews` - Create a new overview
- `PUT /careers/overviews/{id}` - Update an overview
- `DELETE /careers/overviews/{id}` - Delete an overview

### Location Endpoints

- `GET /careers/locations` - Get all locations (with pagination)
- `GET /careers/locations/{id}` - Get a specific location
- `POST /careers/locations` - Create a new location
- `PUT /careers/locations/{id}` - Update a location
- `DELETE /careers/locations/{id}` - Delete a location

## Example Requests

### Create a Roadmap

```bash
curl -X POST "http://localhost:8000/careers/roadmaps" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "career_name": "Software Engineer",
    "milestone": "Learn Python",
    "milestone_description": "Master Python basics",
    "priority": 1
  }'
```

### Get All Roadmaps

```bash
curl "http://localhost:8000/careers/roadmaps?skip=0&limit=10"
```

### Update a Roadmap

```bash
curl -X PUT "http://localhost:8000/careers/roadmaps/1" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "career_name": "Software Engineer",
    "milestone": "Learn Advanced Python",
    "milestone_description": "Master advanced Python concepts",
    "priority": 2
  }'
```

### Delete a Roadmap

```bash
curl -X DELETE "http://localhost:8000/careers/roadmaps/1"
```

## Project Structure

```
PathFinderAI/
├── app/
│   ├── __init__.py           # FastAPI app initialization
│   ├── config.py             # Configuration from environment
│   ├── schemas.py            # Pydantic schemas
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py           # SQLAlchemy declarative base
│   │   └── connection.py     # Database connection setup
│   ├── models/
│   │   ├── __init__.py
│   │   ├── roadmap.py        # RoadMap model
│   │   ├── overview.py       # Overview model
│   │   └── location.py       # Location model
│   ├── routes/
│   │   ├── __init__.py
│   │   └── careers.py        # Career endpoints
│   └── services/
│       ├── __init__.py
│       └── career_service.py # Business logic
├── main.py                    # Application entry point
├── init_db.py                # Database initialization
├── requirements.txt          # Dependencies
├── .env                      # Environment variables
└── README.md                 # Documentation
```

## Features

- **FastAPI Framework**: Modern, fast Python web framework
- **AWS RDS Integration**: MySQL database on AWS RDS
- **SQLAlchemy ORM**: Object-relational mapping
- **Pydantic Validation**: Data validation with type hints
- **Service Layer**: Business logic separation
- **Connection Pooling**: Efficient database connection management
- **Error Handling**: Comprehensive error handling and logging
- **Interactive API Docs**: Swagger UI and ReDoc integration

## Database Schema

### roadmaps Table
```sql
CREATE TABLE roadmaps (
  id INT PRIMARY KEY AUTO_INCREMENT,
  career_name VARCHAR(255) NOT NULL,
  milestone VARCHAR(255) NOT NULL,
  milestone_description VARCHAR(500) NOT NULL,
  priority INT NOT NULL
);
```

### overviews Table
```sql
CREATE TABLE overviews (
  id INT PRIMARY KEY AUTO_INCREMENT,
  career_name VARCHAR(255) NOT NULL,
  avg_salary_range VARCHAR(255) NOT NULL,
  avg_min_degree VARCHAR(255) NOT NULL,
  avg_time_to_complete VARCHAR(255) NOT NULL,
  education_cost VARCHAR(255) NOT NULL,
  alternate_career_names VARCHAR(500)
);
```

### locations Table
```sql
CREATE TABLE locations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  career_name VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL
);
```

## Troubleshooting

### Database Connection Issues
1. Verify AWS RDS endpoint is accessible
2. Check security group allows inbound traffic on port 3306
3. Confirm credentials in `.env` file are correct
4. Test connection: `python -c "from app.database.connection import test_connection; test_connection()"`

### Module Import Errors
1. Ensure all files are in correct directories
2. Verify `__init__.py` files exist in all package directories
3. Install dependencies: `pip install -r requirements.txt`

## License

See LICENSE file for details
