from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services.student.app.main import app as student_app
from src.services.mark.app.main import app as mark_app

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
    "http://dhruvs-macbook-air.local:5173",
    "http://192.168.0.105:5173",
    "https://attendance-extended-front.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.mount("/student", student_app)
app.mount("/mark", mark_app)
