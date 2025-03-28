from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.services.api_parser import ApiParser

router = APIRouter(prefix="/api/bus", tags=["bus"])
api_parser = ApiParser()

class StopIdRequest(BaseModel):
    stop_id: str

class ArrivalTime(BaseModel):
    number: str
    end_stop: str
    arrival_times: List[str]

class ScheduleResponse(BaseModel):
    stop_id: str
    routes: List[ArrivalTime]

@router.post("/schedule", response_model=ScheduleResponse)
async def get_bus_schedule(request: StopIdRequest):
    """
    Get the bus schedule for a specific stop.
    
    Returns the schedule with arrival times for all routes passing through the specified stop.
    """
    try:
        result = api_parser.get_schedule(request.stop_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching schedule: {str(e)}") 