from fastapi import APIRouter
import redis
from config import settings
from fastapi.responses import HTMLResponse

router = APIRouter()
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

@router.post("/start", response_class=HTMLResponse)
async def start_daemon():
    r.xadd(settings.STREAM_NAME, {"command": "START"})
    return """
    <button hx-post="/control/stop" 
            hx-swap="outerHTML" 
            class="bg-red-600 hover:bg-red-700 text-white px-10 py-4 rounded-full font-bold shadow-lg transition-all active:scale-95">
        🛑 ОСТАНОВИТЬ ДЕМОНА
    </button>
    """

@router.post("/stop", response_class=HTMLResponse)
async def stop_daemon():
    r.xadd(settings.STREAM_NAME, {"command": "STOP"})
    return """
    <button hx-post="/control/start" hx-swap="outerHTML" 
            class="bg-green-600 hover:bg-green-500 text-white px-10 py-4 rounded-full font-bold shadow-lg transition-all active:scale-95">
        🚀 ЗАПУСТИТЬ ДЕМОНА
    </button>
    """