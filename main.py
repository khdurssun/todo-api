from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from app.routers.task import router as tasks_router
from database.services import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(title="Task Manager API", lifespan=lifespan)

app.include_router(tasks_router)

@app.get("/")
async def main_page():
    return {"message": "Task Manager API is ready!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)