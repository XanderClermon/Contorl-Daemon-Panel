from fastapi import FastAPI
from routes import ui, control

app = FastAPI()

app.include_router(ui.router)
app.include_router(control.router, prefix="/control", tags=["Management"])

# uvicorn main:app --reload