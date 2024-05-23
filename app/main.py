from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/images", StaticFiles(directory="templates/images"), name="images")
app.mount('/css', StaticFiles(directory="templates/css"), name='css')
app.mount('/vec_img', StaticFiles(directory="templates/vec_img"), name='vec_img')
app.mount('/scss', StaticFiles(directory="templates/scss"), name='scss')
app.mount('/fonts', StaticFiles(directory="templates/fonts"), name='fonts')


templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

