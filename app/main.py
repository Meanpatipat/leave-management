from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.leave import router as leave_router
from app.routes.manager import router as manager_router

app = FastAPI()

# 🔧 FIX CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # อนุญาตทุก origin (dev เท่านั้น)
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, PUT, DELETE ฯลฯ
    allow_headers=["*"],          # Authorization, Content-Type ฯลฯ
)

app.include_router(leave_router)
app.include_router(manager_router)
