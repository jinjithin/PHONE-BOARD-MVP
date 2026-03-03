from fastapi import FastAPI
from app.routes.telemetry import router as telemetry_router

app = FastAPI()

app.include_router(telemetry_router)

@app.get("/")
def root():
    return {"message": "Device Monitor API running"}