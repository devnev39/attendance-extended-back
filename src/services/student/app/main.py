from fastapi import FastAPI
from src.services.student.app.api.router import router

app = FastAPI(
    title= "Student management server",
)

app.include_router(router=router, prefix="/api/v1")