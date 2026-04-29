from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Job Application Agent")
app.include_router(router)
