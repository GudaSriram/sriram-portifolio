import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

MAIN_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


templates = Jinja2Templates("templates")

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
 

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})
