from pydantic import BaseModel
from typing import Dict, List, Optional, Any


class AIAnalysisRequest(BaseModel):

    user_id: str


class AIAnalysisResponse(BaseModel):

    user_id: str

    cognitive_score: Optional[float] = None

    performance_level: Optional[str] = None

    weakest_area: Optional[str] = None

    overall_trend: Optional[str] = None

    recommended_activity: Optional[str] = None

    details: Optional[Dict[str, Any]] = None