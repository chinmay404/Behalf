# app/api.py
import base64
import uuid
import asyncio
import aiofiles
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .utils import process_response, save_audio_file
from .models import ConfigRequest, ResponseConfigs


router = APIRouter()


@router.post("/conversation")
async def conversation_endoint(conversion_id: str, config: ConfigRequest, ResponseConfigs: ResponseConfigs, audio: UploadFile = File(...)):
    """
    Endpoint to receive an audio file along with user_id and conversion_id,
    processes the audio in memory, and returns AI response text and a TTS audio file
    encoded as a Base64 string.
    """
    try:
        audio_bytes = await audio.read()

        unique_id = uuid.uuid4().hex
        filename = asyncio.create_task(save_audio_file(
            config.user_id, conversion_id, audio_bytes))
        if filename is None:
            raise HTTPException(
                status_code=500, detail="Failed to save audio file.")
        else:
            try:
                Response = process_response(config.user_id,
                                            conversion_id,
                                            filename)
            except Exception as e:
                raise HTTPException(
                    status_code=500, detail=f"AI Respinse or Audio processing failed: {str(e)}")

            # encoded_audio = base64.b64encode(process_response).decode("utf-8")

            return JSONResponse(
                status_code=200,
                content={
                    "user_id": config.user_id,
                    "conversion_id": conversion_id,
                    "transcript": Response.transcript,
                    "translation": "Translated text here",
                    "processed_audio": Response.encoded_audio
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
