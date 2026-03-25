from fastapi import FastAPI
from app.database import test_connection
from app.routes.careers import router as careers_router
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PathFinder API",
    description="API with service layer and AWS RDS MySQL integration",
    version="1.0.0"
)

# Include routers
app.include_router(careers_router)

@app.on_event("startup")
async def startup_event():
    """Test database connection on startup"""
    logger.info("Starting up application...")
    if test_connection():
        logger.info("Database connection successful")
    else:
        logger.error("Database connection failed")

@app.get("/", tags=["health"])
def read_root():
    """Root endpoint"""
    return {"message": "PathFinder API is running"}

@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
