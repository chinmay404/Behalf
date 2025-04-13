# app/api.py
import base64
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .utils import process_audio_in_memory
from .models import ConfigRequest
router = APIRouter()

@router.post("/audio_input")
async def process_audio_endpoint(user_id: str, conversion_id: str,config : ConfigRequest , audio: UploadFile = File(...)):
    """
    Endpoint to receive an audio file along with user_id and conversion_id,
    processes the audio in memory, and returns AI response text and a TTS audio file
    encoded as a Base64 string.
    """
    try:
        audio_bytes = await audio.read()
    
        unique_id = uuid.uuid4().hex


        try:
            transcript, processed_audio_bytes = process_audio_in_memory(user_id,
                                                                        conversion_id,
                                                                        audio_bytes)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"AI Respinse or Audio processing failed: {str(e)}")

        encoded_audio = base64.b64encode(processed_audio_bytes).decode("utf-8")
        
        return JSONResponse(
            status_code=200,
            content={
                "user_id": user_id,
                "conversion_id": conversion_id,
                "transcript": transcript,
                "processed_audio": encoded_audio  
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router.post("/getTTS")
def get_tts(user_id: str, conversion_id: str, text: str):
    """
    Endpoint to get TTS audio encoded as a Base64 string.
    """
    try:

        dummy_audio_bytes = b"Dummy audio data for TTS."
        encoded_audio = base64.b64encode(dummy_audio_bytes).decode("utf-8")
        
        return JSONResponse(
            status_code=200,
            content={
                "tts": encoded_audio  
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 