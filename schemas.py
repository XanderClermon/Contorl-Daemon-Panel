from pydantic import BaseModel
from typing import Optional

class CommandRequest(BaseModel):
    command: str          # "START", "STOP", "UPDATE_CONFIG"
    value: Optional[str] = None
    sender: str = "web_ui"