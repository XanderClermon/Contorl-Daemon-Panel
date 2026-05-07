from fastapi import FastAPI, HTTPException
import redis

app = FastAPI(title="Signal Tower Control")

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Универсальная функция для записи в стрим
def push_to_stream(command: str, value: str = None):
    try:
        msg_id = r.xadd(
            "signal:commands",
            {"command": command, "value": str(value) if value else "none", "sender": "web_api"}
        )
        return msg_id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis Error: {str(e)}")

@app.post("/start")
async def start_daemon():
    """Отправляет команду на запуск сканирования"""
    mid = push_to_stream("START")
    return {"status": "Command START sent", "id": mid}

@app.post("/stop")
async def stop_daemon():
    """Отправляет команду на остановку сканирования"""
    mid = push_to_stream("STOP")
    return {"status": "Command STOP sent", "id": mid}

@app.get("/health")
async def health():
    return {"status": "online", "redis": r.ping()}