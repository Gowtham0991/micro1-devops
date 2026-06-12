from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Micro1 DevOps Assignment",
    version="1.0.0"
)

Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "service": "micro1-devops-assignment",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def readiness():
    return {"status": "ready"}

@app.get("/api/v1/info")
def info():
    return {
        "service": "micro1-devops-assignment",
        "version": "1.0.0",
        "environment": "production"
    }
