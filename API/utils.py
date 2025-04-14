# app/utils.py
import io
from Agent.graph import get_graph , invoke_graph
import aiofiles



async def save_audio_file(user_id: str, conversation_id: str, audio_bytes: bytes):
    filename = f"{user_id}_{conversation_id}.mp3"
    try:
        async with aiofiles.open(filename, "wb") as file:
            await file.write(audio_bytes)
            return filename
    except Exception as e:
        print(f"Failed to save audio file {filename}: {e}")
        
        
        
        

def process_response(user_id:str ,
                    conversion_id:str,
                    filename: str):
    """
    Processes the given audio bytes in memory and returns a transcript along with
    processed audio bytes (for example, after applying a text-to-speech routine).

    Parameters:
    - audio_bytes: The raw bytes from the uploaded audio file.
    - conversion_id: Conversation ID.
    - filename: Audio File Name.

    Returns:
    - transcript: The transcript text generated from the audio.
    - processed_audio: The processed audio bytes (could be modified as per your logic).
    """
    
    
    return transcript, 
 
 
 
# g = get_graph()
# messges = [HumanMessage(
#     content="i wnat to talk with this German person about getrting apples in very cheap price")]

# config = {"configurable": {"thread_id": "1234"}}
# res = g.invoke({"messages": messges,
#                 "goal": "I want to talk with this German person about getting apples in very cheap price",
#                 "UserLang": "en",
#                 "OtherPersonLang": "de",
#                 "Plan": None,
#                 "invoked_by": "User"} , config=config)
