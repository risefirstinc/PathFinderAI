from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.career_service import RoadMapService, OverviewService, LocationService
from app.schemas import RoadMap as RoadMapSchema, Overview as OverviewSchema, Location as LocationSchema

router = APIRouter(prefix="/careers", tags=["careers"])

# ==================== RoadMap Endpoints ====================

@router.get("/roadmaps", response_model=list[RoadMapSchema])
def get_roadmaps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all roadmaps with pagination"""
    roadmaps = RoadMapService.get_all(db, skip=skip, limit=limit)
    return roadmaps


@router.get("/roadmaps/{roadmap_id}", response_model=RoadMapSchema)
def get_roadmap_by_id(roadmap_id: int, db: Session = Depends(get_db)):
    """Get a specific roadmap by ID"""
    roadmap = RoadMapService.get_by_id(db, roadmap_id)
    if not roadmap:
        raise HTTPException(status_code=404, detail="RoadMap not found")
    return roadmap


@router.get("/roadmaps/career_name/{career_name}", response_model=list[RoadMapSchema])
def get_roadmap_by_career_name(career_name: str, db: Session = Depends(get_db)):
    roadmaps = RoadMapService.get_by_career_name(db, career_name)
    if not roadmaps:
        raise HTTPException(status_code=404, detail="RoadMap not found")
    return roadmaps


@router.post("/roadmaps", response_model=RoadMapSchema, status_code=status.HTTP_201_CREATED)
def create_roadmap(roadmap: RoadMapSchema, db: Session = Depends(get_db)):
    """Create a new roadmap"""
    return RoadMapService.create(db, roadmap)


@router.put("/roadmaps/{roadmap_id}", response_model=RoadMapSchema)
def update_roadmap(roadmap_id: int, roadmap: RoadMapSchema, db: Session = Depends(get_db)):
    """Update an existing roadmap"""
    updated_roadmap = RoadMapService.update(db, roadmap_id, roadmap)
    if not updated_roadmap:
        raise HTTPException(status_code=404, detail="RoadMap not found")
    return updated_roadmap


@router.delete("/roadmaps/{roadmap_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_roadmap(roadmap_id: int, db: Session = Depends(get_db)):
    """Delete a roadmap"""
    if not RoadMapService.delete(db, roadmap_id):
        raise HTTPException(status_code=404, detail="RoadMap not found")


# ==================== Overview Endpoints ====================

@router.get("/overviews", response_model=list[OverviewSchema])
def get_overviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all overviews with pagination"""
    overviews = OverviewService.get_all(db, skip=skip, limit=limit)
    return overviews


@router.get("/overviews/{overview_id}", response_model=OverviewSchema)
def get_overview_by_id(overview_id: int, db: Session = Depends(get_db)):
    """Get a specific overview by ID"""
    overview = OverviewService.get_by_id(db, overview_id)
    if not overview:
        raise HTTPException(status_code=404, detail="Overview not found")
    return overview


@router.post("/overviews", response_model=OverviewSchema, status_code=status.HTTP_201_CREATED)
def create_overview(overview: OverviewSchema, db: Session = Depends(get_db)):
    """Create a new overview"""
    return OverviewService.create(db, overview)


@router.put("/overviews/{overview_id}", response_model=OverviewSchema)
def update_overview(overview_id: int, overview: OverviewSchema, db: Session = Depends(get_db)):
    """Update an existing overview"""
    updated_overview = OverviewService.update(db, overview_id, overview)
    if not updated_overview:
        raise HTTPException(status_code=404, detail="Overview not found")
    return updated_overview


@router.delete("/overviews/{overview_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_overview(overview_id: int, db: Session = Depends(get_db)):
    """Delete an overview"""
    if not OverviewService.delete(db, overview_id):
        raise HTTPException(status_code=404, detail="Overview not found")


# ==================== Location Endpoints ====================

@router.get("/locations", response_model=list[LocationSchema])
def get_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all locations with pagination"""
    locations = LocationService.get_all(db, skip=skip, limit=limit)
    return locations


@router.get("/locations/{location_id}", response_model=LocationSchema)
def get_location_by_id(location_id: int, db: Session = Depends(get_db)):
    """Get a specific location by ID"""
    location = LocationService.get_by_id(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.post("/locations", response_model=LocationSchema, status_code=status.HTTP_201_CREATED)
def create_location(location: LocationSchema, db: Session = Depends(get_db)):
    """Create a new location"""
    return LocationService.create(db, location)


@router.put("/locations/{location_id}", response_model=LocationSchema)
def update_location(location_id: int, location: LocationSchema, db: Session = Depends(get_db)):
    """Update an existing location"""
    updated_location = LocationService.update(db, location_id, location)
    if not updated_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated_location


@router.delete("/locations/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    """Delete a location"""
    if not LocationService.delete(db, location_id):
        raise HTTPException(status_code=404, detail="Location not found")