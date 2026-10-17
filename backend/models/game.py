from pydantic import BaseModel
from typing import Optional


class GameCreate(BaseModel):

    name: str

    description: Optional[str] = None

    category: Optional[str] = None

    difficulty: Optional[str] = "easy"


class GameResponse(GameCreate):

    id: int

    class Config:
        from_attributes = True