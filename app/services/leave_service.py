from datetime import datetime, timedelta

from app.firebase import db


def days_between(start: str, end: str):
    start_date = datetime.fromisoformat(start)
    end_date = datetime.fromisoformat(end)
    return (end_date - start_date).days + 1


def check_overlap(user_id, start, end):
    requests = (
        db.collection("leave_requests")
        .where("user_id", "==", user_id)
        .where("status", "in", ["Pending", "Approved"])
        .stream()
    )

    for r in requests:
        data = r.to_dict()
        if not (end < data["start_date"] or start > data["end_date"]):
            return True
    return False


def submit_leave(user_id, payload):
    if check_overlap(user_id, payload["start_date"], payload["end_date"]):
        raise Exception("Leave dates overlap")

    days = days_between(payload["start_date"], payload["end_date"])
    if payload["leave_type"] == "Sick Leave":
        leave_type = "sick"
    else:
        leave_type = "annaul"

    doc_id = f"{user_id}_{leave_type}"
    balance_ref = db.collection("leave_balances").document(doc_id).get()

    if not balance_ref.exists:
        raise Exception("Leave balance not found")

    balance = balance_ref.to_dict()
    if balance["remaining"] < days:
        raise Exception("Insufficient leave balance")

    db.collection("leave_requests").add(
        {
            "user_id": user_id,
            "leave_type": payload["leave_type"],
            "start_date": payload["start_date"],
            "end_date": payload["end_date"],
            "days": days,
            "status": "Pending",
        }
    )