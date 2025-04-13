from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ConfigRequest(BaseModel):
    """
    Request model for configuration.
    """
    initial: bool = Field(default=False, description="Indicates if this is the initial configuration request.")
    Userlanguage: Optional[str] = Field(default=None, description="Language preference of the user.")
    OtherPersonlanguage: Optional[str] = Field(default=None, description="Language preference of Another Person.")