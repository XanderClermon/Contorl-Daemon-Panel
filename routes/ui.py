from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import redis
from config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Подключаем Redis (локально для этого роутера)
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Отдает каркас страницы"""
    return templates.TemplateResponse(
        request=request,
        name="base.html"
    )

@router.get("/tab/main", response_class=HTMLResponse)
async def get_main_tab(request: Request):
    """Контент вкладки 'Главная'"""
    try:
        r.ping()
        status, color = "Online", "text-green-400"
    except:
        status, color = "Offline", "text-red-400"

    return f"""
    <div class="animate-fade-in p-6 bg-gray-900 rounded-2xl border border-gray-700">
        <h2 class="text-xl font-bold mb-4">Системный монитор</h2>
        <div class="flex items-center space-x-3">
            <span class="text-gray-400">Redis Status:</span>
            <span class="font-mono font-bold {color}">{status}</span>
        </div>
    </div>
    """

@router.get("/tab/netpanel", response_class=HTMLResponse)
async def get_netpanel_tab(request: Request):
    """Контент вкладки 'NetPanel'"""
    return templates.TemplateResponse(
        request=request,
        name="partials/net_panel.html"
    )