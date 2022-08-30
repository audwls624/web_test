import uvicorn
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/home/{item_id}", response_class=HTMLResponse)
async def render_main(request: Request, item_id: int):
    return templates.TemplateResponse('index.html', context={'request': request, "item_id": item_id})


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
