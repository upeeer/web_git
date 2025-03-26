from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TT_orm
from api.student import student
from fastapi import Request
from fastapi.templating import Jinja2Templates
from basic_data import *

user=FastAPI()
template = Jinja2Templates(directory="templates")
register_tortoise(
    app=user,
    config=TT_orm
)

user.include_router(student,prefix="/student",tags=["学生数据"])

@user.get("/index") #前端交接处
def index(request: Request):
    import os
    print(os.path.abspath("templates"))
    name = 'hhhb'
    password = 234
    return template.TemplateResponse(
        "jstext.html",
        {
            "request": request,
            "username": name,
            "password": password
        },
    )

if __name__ == "__main__":
    uvicorn.run("main:user", port=8080, reload=True)