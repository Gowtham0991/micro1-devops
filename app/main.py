from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.logging_config import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Micro1 DevOps Assignment",
    version="1.0.0",
    description="Production-style backend service built for Micro1 DevOps Assessment"
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "service": "micro1-devops-assignment",
        "status": "running"
    }


@app.get("/health")
def health():
    logger.info("Health check requested")

    return {
        "status": "healthy"
    }


@app.get("/ready")
def readiness():
    logger.info("Readiness check requested")

    return {
        "status": "ready"
    }


@app.get("/api/v1/info")
def info():
    logger.info("Info endpoint requested")

    return {
        "service": "micro1-devops-assignment",
        "version": "1.0.0",
        "environment": "production"
    }
