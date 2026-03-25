"""
Sample test script to verify API endpoints are working
Run this after starting the API server
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")


def test_create_roadmap():
    """Test creating a roadmap"""
    print("\n=== Creating Roadmap ===")
    data = {
        "id": 1,
        "career_name": "Software Engineer",
        "milestone": "Learn Python Basics",
        "milestone_description": "Master Python fundamentals and syntax",
        "priority": 1
    }
    response = requests.post(f"{BASE_URL}/careers/roadmaps", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.json().get("id") if response.status_code == 201 else None


def test_get_roadmaps():
    """Test getting all roadmaps"""
    print("\n=== Getting All Roadmaps ===")
    response = requests.get(f"{BASE_URL}/careers/roadmaps?skip=0&limit=10")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_get_roadmap(roadmap_id):
    """Test getting a specific roadmap"""
    print(f"\n=== Getting Roadmap {roadmap_id} ===")
    response = requests.get(f"{BASE_URL}/careers/roadmaps/{roadmap_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_update_roadmap(roadmap_id):
    """Test updating a roadmap"""
    print(f"\n=== Updating Roadmap {roadmap_id} ===")
    data = {
        "id": roadmap_id,
        "career_name": "Senior Software Engineer",
        "milestone": "Learn Advanced Python",
        "milestone_description": "Master advanced Python concepts and patterns",
        "priority": 2
    }
    response = requests.put(f"{BASE_URL}/careers/roadmaps/{roadmap_id}", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_create_overview():
    """Test creating an overview"""
    print("\n=== Creating Overview ===")
    data = {
        "id": 1,
        "career_name": "Software Engineer",
        "avg_salary_range": "$100,000 - $150,000",
        "avg_min_degree": "Bachelor's in Computer Science",
        "avg_time_to_complete": "4 years",
        "education_cost": "$20,000 - $100,000",
        "alternate_career_names": "Developer, Programmer"
    }
    response = requests.post(f"{BASE_URL}/careers/overviews", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_create_location():
    """Test creating a location"""
    print("\n=== Creating Location ===")
    data = {
        "id": 1,
        "career_name": "Software Engineer",
        "location": "San Francisco, CA"
    }
    response = requests.post(f"{BASE_URL}/careers/locations", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_delete_roadmap(roadmap_id):
    """Test deleting a roadmap"""
    print(f"\n=== Deleting Roadmap {roadmap_id} ===")
    response = requests.delete(f"{BASE_URL}/careers/roadmaps/{roadmap_id}")
    print(f"Status: {response.status_code}")


if __name__ == "__main__":
    print("PathFinder API Test Suite")
    print("=" * 50)
    
    try:
        # Test health check
        test_health()
        
        # Test Roadmap operations
        roadmap_id = test_create_roadmap()
        if roadmap_id:
            test_get_roadmaps()
            test_get_roadmap(roadmap_id)
            test_update_roadmap(roadmap_id)
        
        # Test Overview operations
        test_create_overview()
        
        # Test Location operations
        test_create_location()
        
        # Test delete
        if roadmap_id:
            test_delete_roadmap(roadmap_id)
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to API server.")
        print("Make sure the server is running: python main.py")
    except Exception as e:
        print(f"ERROR: {str(e)}")
