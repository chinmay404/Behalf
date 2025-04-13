# app/utils.py
import io
from Agent.graph import get_graph , invoke_graph

def process_audio_in_memory(user_id:str ,
                            conversion_id:str,
                            audio_bytes: bytes) -> (str, bytes):
    """
    Processes the given audio bytes in memory and returns a transcript along with
    processed audio bytes (for example, after applying a text-to-speech routine).

    Parameters:
    - audio_bytes: The raw bytes from the uploaded audio file.

    Returns:
    - transcript: The transcript text generated from the audio.
    - processed_audio: The processed audio bytes (could be modified as per your logic).
    """
    # Replace the following logic with your actual audio processing routines.
    # invoke_graph(user_id, conversion_id, audio_bytes)
    transcript = "This is a dummy transcript generated from the provided audio."
    
    # For demonstration, we assume the processed audio is the same as the input.
    processed_audio = audio_bytes
    return transcript, processed_audio
 
 
 
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
