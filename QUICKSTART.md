# Quick Start Guide - PathFinder API with AWS RDS

## 🚀 Fast Setup (5 minutes)

### Step 1: Configure AWS RDS Credentials
Edit `.env` file with your AWS RDS details:
```env
DB_HOST=your-rds-instance.rds.amazonaws.com
DB_PORT=3306
DB_USER=admin
DB_PASSWORD=your_password
DB_NAME=pathfinder_db
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Initialize Database
```bash
python init_db.py
```

### Step 4: Start the Server
```bash
python main.py
```

✅ API is now running at `http://localhost:8000`

---

## 📚 Test the API

### Option 1: Interactive Documentation
Open in browser: `http://localhost:8000/docs`

### Option 2: Run Test Script
```bash
python test_api.py
```

### Option 3: Use cURL

**Create a Roadmap:**
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

**Get All Roadmaps:**
```bash
curl "http://localhost:8000/careers/roadmaps"
```

**Get Specific Roadmap:**
```bash
curl "http://localhost:8000/careers/roadmaps/1"
```

**Update Roadmap:**
```bash
curl -X PUT "http://localhost:8000/careers/roadmaps/1" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "career_name": "Senior Software Engineer",
    "milestone": "Learn Advanced Python",
    "milestone_description": "Master advanced patterns",
    "priority": 2
  }'
```

**Delete Roadmap:**
```bash
curl -X DELETE "http://localhost:8000/careers/roadmaps/1"
```

---

## 📋 Complete API Reference

### Roadmaps
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/careers/roadmaps` | List all roadmaps |
| GET | `/careers/roadmaps/{id}` | Get specific roadmap |
| POST | `/careers/roadmaps` | Create roadmap |
| PUT | `/careers/roadmaps/{id}` | Update roadmap |
| DELETE | `/careers/roadmaps/{id}` | Delete roadmap |

### Overviews
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/careers/overviews` | List all overviews |
| GET | `/careers/overviews/{id}` | Get specific overview |
| POST | `/careers/overviews` | Create overview |
| PUT | `/careers/overviews/{id}` | Update overview |
| DELETE | `/careers/overviews/{id}` | Delete overview |

### Locations
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/careers/locations` | List all locations |
| GET | `/careers/locations/{id}` | Get specific location |
| POST | `/careers/locations` | Create location |
| PUT | `/careers/locations/{id}` | Update location |
| DELETE | `/careers/locations/{id}` | Delete location |

---

## 🔧 Troubleshooting

**Error: Cannot connect to database**
- ✓ Check AWS RDS endpoint in `.env`
- ✓ Verify security group allows port 3306
- ✓ Confirm credentials are correct
- ✓ Test: `python init_db.py`

**Error: Module not found**
- ✓ Install dependencies: `pip install -r requirements.txt`
- ✓ Ensure Python 3.9+ is installed

**Error: Table not found**
- ✓ Run: `python init_db.py` to create tables

---

## 📁 Project Structure
```
PathFinderAI/
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── services/        # Business logic
│   ├── routes/          # API endpoints
│   ├── database/        # DB connection
│   └── schemas.py       # Pydantic models
├── main.py              # Entry point
├── init_db.py           # Database setup
├── test_api.py          # Test script
├── .env                 # Config (update with AWS credentials!)
└── requirements.txt     # Dependencies
```

---

## 📖 Documentation Files
- `SETUP.md` - Detailed setup guide
- `IMPLEMENTATION_SUMMARY.md` - Technical overview
- `README.md` - Project information

---

## 🎯 What's Included

✅ AWS RDS MySQL integration
✅ Full CRUD APIs for 3 resources
✅ Service layer architecture
✅ Error handling & logging
✅ Input validation
✅ Connection pooling
✅ Interactive API docs (Swagger UI)
✅ Test script included

---

## 🆘 Getting Help

1. Check `SETUP.md` for detailed configuration
2. Review `IMPLEMENTATION_SUMMARY.md` for architecture
3. Visit `http://localhost:8000/docs` for interactive API docs
4. Run `python test_api.py` to verify setup

Ready to go! Start by running `python main.py` 🚀
