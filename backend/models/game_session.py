from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class GameScore(BaseModel):

    patient_id: int

    game_name: str

    score: int

    accuracy: float

    time_taken: float

    difficulty: str

    played_at: Optional[datetime] = None