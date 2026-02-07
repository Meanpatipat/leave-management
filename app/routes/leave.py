from fastapi import APIRouter

from app.services.leave_service import submit_leave

router = APIRouter(prefix="/leave", tags=["Leave"])


@router.post("/request")
def request_leave(data: dict):
    submit_leave(data["name"], data)
    return {"message": "Leave request received", "data": data}