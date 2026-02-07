from app.firebase import db

# Users
db.collection("users").document("emp001").set({
    "name": "Employee One",
    "role": "employee"
})

db.collection("users").document("mgr001").set({
    "name": "Manager One",
    "role": "manager"
})

# Leave Types
db.collection("leave_types").document("annual").set({
    "name": "Annual Leave"
})

db.collection("leave_types").document("sick").set({
    "name": "Sick Leave"
})

# Leave Balances (ใช้ custom document ID)
db.collection("leave_balances").document("emp001_annual").set({
    "user_id": "emp001",
    "leave_type": "annual",
    "remaining": 10
})

db.collection("leave_balances").document("emp001_sick").set({
    "user_id": "emp001",
    "leave_type": "sick",
    "remaining": 5
})
