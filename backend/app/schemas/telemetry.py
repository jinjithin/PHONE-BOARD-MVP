from pydantic import BaseModel
from datetime import datetime


class TelemetryCreate(BaseModel):
    device_id: str
    battery_percent: int
    timestamp: datetime