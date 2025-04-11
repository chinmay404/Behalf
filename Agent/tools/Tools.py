from langchain_core.tools import tool
from Agent.speech_and_audios import speech_main
from Agent.speech_and_audios import tts
# TODO : Add TTS and STT here for Take inp and output


@tool
def get_user_input(what_to_ask: str) -> str:
    """Get input from user."""
    tts.text_to_speech_eleven_labs(what_to_ask)
    print(f"FROM LLM TO USER : {what_to_ask}")
    print("Recording your input...")
    inp = speech_main.record_and_transcribe()
    return inp


@tool
def get_other_person_input(what_to_ask: str) -> str:
    """Get other person input."""
    tts.text_to_speech_eleven_labs(what_to_ask)
    print(f"FROM LLM TO OTHER-USER : {what_to_ask}")
    inp = input("Enter your input here:\n")
    return inp


ToolList = [
    get_user_input,
    get_other_person_input,
]
