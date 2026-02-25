from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.career_service import RoadMapService, OverviewService, LocationService
from app.schemas import RoadMap as RoadMapSchema, Overview as OverviewSchema, Location as LocationSchema

router = APIRouter(prefix="/careers", tags=["careers"])

# RoadMap endpoints
@router.get("/roadmaps", response_model=list[RoadMapSchema])
def get_roadmaps(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	roadmaps = RoadMapService.get_all(db, skip=skip, limit=limit)
	return roadmaps

@router.get("/roadmaps/{roadmap_id}", response_model=RoadMapSchema)
def get_roadmap_by_id(roadmap_id: int, db: Session = Depends(get_db)):
	roadmap = RoadMapService.get_by_id(db, roadmap_id)
	if not roadmap:
		raise HTTPException(status_code=404, detail="RoadMap not found")
	return roadmap

# Overview endpoints
@router.get("/overviews", response_model=list[OverviewSchema])
def get_overviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	overviews = OverviewService.get_all(db, skip=skip, limit=limit)
	return overviews

@router.get("/overviews/{overview_id}", response_model=OverviewSchema)
def get_overview_by_id(overview_id: int, db: Session = Depends(get_db)):
	overview = OverviewService.get_by_id(db, overview_id)
	if not overview:
		raise HTTPException(status_code=404, detail="Overview not found")
	return overview

# Location endpoints
@router.get("/locations", response_model=list[LocationSchema])
def get_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	locations = LocationService.get_all(db, skip=skip, limit=limit)
	return locations

@router.get("/locations/{location_id}", response_model=LocationSchema)
def get_location_by_id(location_id: int, db: Session = Depends(get_db)):
	location = LocationService.get_by_id(db, location_id)
	if not location:
		raise HTTPException(status_code=404, detail="Location not found")
	return location