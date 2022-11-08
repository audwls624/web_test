import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import router_main
from sql_app import models
from sql_app.database import engine

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
models.Base.metadata.create_all(bind=engine)

app.include_router(router_main.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
