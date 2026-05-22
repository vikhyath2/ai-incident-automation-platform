from pydantic import BaseModel


class IncidentRequest(BaseModel):
    log_text: str