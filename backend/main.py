from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ==========================================
# DATABASE
# ==========================================

from services.database import create_database


# ==========================================
# ROUTES
# ==========================================

from routes.patients import router as patients_router
from routes.games import router as games_router
from routes.reminders import router as reminders_router
from routes.memories import router as memories_router
from routes.family import router as family_router
from routes.game_session import router as game_session_router
from routes.cognitive import router as cognitive_router
from routes.caregivers import router as caregivers_router
from routes.ai import router as ai_router


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(
    title="NIRVANA API",
    description="AI-Based Cognitive Gaming and Memory Assistance Platform",
    version="1.0.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# CREATE DATABASE
# ==========================================

@app.on_event("startup")
def startup_event():

    create_database()

    print("======================================")
    print("NIRVANA Backend Started Successfully 🚀")
    print("Database Created Successfully 🗄️")
    print("======================================")


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to NIRVANA Backend 🚀",
        "project": "SIH 26003",
        "status": "Backend is running successfully"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "NIRVANA API is running successfully"
    }


# ==========================================
# INCLUDE ROUTERS
# ==========================================

app.include_router(patients_router)
app.include_router(games_router)
app.include_router(reminders_router)
app.include_router(memories_router)
app.include_router(family_router)
app.include_router(game_session_router)
app.include_router(cognitive_router)
app.include_router(caregivers_router)
app.include_router(ai_router)


# ==========================================
# API INFORMATION
# ==========================================

@app.get("/api-info")
def api_info():

    return {
        "project": "NIRVANA SIH 26003",

        "modules": [
            "Patients",
            "Games",
            "Reminders",
            "Memory Assistance",
            "Family",
            "Game Sessions",
            "Cognitive Analysis",
            "Caregiver Support",
            "AI Engine"
        ],

        "documentation": "/docs"
    }