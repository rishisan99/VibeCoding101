from fastapi import FastAPI

from finance_coach_agent.api.routes import router

app = FastAPI(title="Finance Coach Agent")
app.include_router(router)
