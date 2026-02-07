from pydantic import BaseModel
from datetime import date

class LeaveRequestCreate(BaseModel):
    leave_type: str
    start_date: date
    end_date: date
