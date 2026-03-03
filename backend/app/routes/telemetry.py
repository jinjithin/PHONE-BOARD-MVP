from fastapi import APIRouter
from app.schemas.telemetry import TelemetryCreate

router = APIRouter()


@router.post("/telemetry")
def create_telemetry(payload: TelemetryCreate):
    print("Received telemetry:", payload)
    return {"status": "success"}