# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(router)

# Run: uvicorn main:app --reload
