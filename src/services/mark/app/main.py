from fastapi import FastAPI
from src.services.mark.app.api.router import router

app = FastAPI(
    title= "Mark management server",
)

app.include_router(router=router, prefix="/api/v1")