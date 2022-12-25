""" 
main app for project
"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")


# TODO add logging for better debugging

# TODO create signup model and HTML page

# TODO create login model and HTML page

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})