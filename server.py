from fastapi import FastAPI
from src.services.student.app.main import app as student_app

app = FastAPI()

app.mount("/student", student_app)
