from fastapi import APIRouter
from app.firebase import db

router = APIRouter(prefix="/manager", tags=["Manager"])

@router.get("/pending")
def pending_requests():
    docs = db.collection("leave_requests") \
        .where("status", "==", "Pending") \
        .stream()
    return [d.to_dict() | {"id": d.id} for d in docs]


@router.patch("/approve/{request_id}")
def approve(request_id: str):
    ref = db.collection("leave_requests").document(request_id)
    req = ref.get().to_dict()

    balance_ref = db.collection("leave_balances") \
        .where("user_id", "==", req["user_id"]) \
        .where("leave_type", "==", req["leave_type"]) \
        .limit(1).get()

    balance_doc = balance_ref[0]
    balance_ref = balance_doc.reference

    balance_ref.update({
        "remaining": balance_doc.to_dict()["remaining"] - req["days"]
    })

    ref.update({"status": "Approved"})
    return {"message": "Approved"}
