from typing import Optional
from pydantic import BaseModel, Field
from _init_LLMS_ import get_groq_llm
from speech_and_audios.speech_main import record_and_transcribe

class SituationInforamtionExtract(BaseModel):
    """Extracted information from given user input."""
    situation: str = Field(description="The Situation in which the user in ealaborate a little")
    opposite_party: str = Field(description="The Opposite Party with whom user want to communicate")
    goal_of_communication: str = Field(description="The Goal Of Communication")
    expected_output : str = Field(description="The Expected Output of the Communication")
    


def get_info(user_input: str):
    try:
        llm = get_groq_llm()
        structured_llm = llm.with_structured_output(SituationInforamtionExtract)
        output = structured_llm.invoke(user_input)
        
        dict_output = output.__dict__ if hasattr(output, "__dict__") else dict(output)
        return dict_output
        
    except Exception as e : 
        print(e)
