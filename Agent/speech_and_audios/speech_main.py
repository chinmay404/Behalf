from .record_audio import record_audio
from groq import Groq
from .stt import get_transcription
import os
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("groq_api_key")
client = Groq(api_key=api_key)


def record_and_transcribe():
    # while True:
    try:
        # user_input = input("Press Enter to start recording or type 'q' to exit: ").strip().lower()
        # if user_input == 'q':
        #     print("Exiting P_AI. Goodbye!")
        #     break
        audio_path = record_audio()
        transcript = get_transcription(audio_path, client)
        return transcript
    except Exception as e:
        print(f"Error: {e}")


def record_and_transcribe():
    try:
        transcript = get_transcription(audio_path, client)
        return transcript
    except Exception as e:
        print(f"Error: {e}")