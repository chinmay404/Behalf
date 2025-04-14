from pydantic import BaseModel, Field , confloat
from typing import Optional, Dict, Any

class ConfigRequest(BaseModel):
    """
    Request model for configuration.
    """
    user_id: str = Field(..., description="Unique identifier for the user.")
    initial: bool = Field(default=False, description="Indicates if this is the initial configuration request.")
    Userlanguage: str = Field(description="Language preference of the user.")
    OtherPersonlanguage: str = Field(description="Language preference of Another Person.")
    

class ResponseConfigs(BaseModel):
    """
    Tailored response model for configuration.
    """
    FriendlyToFormal: float = Field(..., ge=0.0, le=1.0, description="Friendly or Formal score for the response.")

