from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services.student.app.main import app as student_app

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.mount("/student", student_app)
