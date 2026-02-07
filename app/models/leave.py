from fastapi import APIRouter, Depends
from app.schemas.leave_request import LeaveRequestCreate
from app.services.leave_service import submit_leave

router = APIRouter(prefix="/leaves", tags=["Employee"])

@router.post("/")
def request_leave(
    payload: LeaveRequestCreate,
    user_id: str = "emp001"  # mock auth
):
    submit_leave(user_id, payload)
    return {"message": "Leave request submitted"}
