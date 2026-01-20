from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory="/templates")

@router.get("/post/{post_name}")
async def show_post(request: Request, post_name: str):
    post_path = f"/posts/{post_name}.html"
    if os.path.exists(post_path):
        return templates.TemplateResponse(f"../posts/{post_name}.html", {"request":request})
    return {"error":"Post not found"}