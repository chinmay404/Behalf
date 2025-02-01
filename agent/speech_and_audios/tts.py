import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from playsound import playsound
import pyttsx3


def play_mp3(file_path):
    playsound(file_path)


engine = pyttsx3.init()


def text_to_speech_eleven_labs(text: str) -> str:
    # Load API key from .env
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("elevenlabs_api_key")
    if not api_key:
        print("Error: API key not found in .env file.")
        return None

    client = ElevenLabs(api_key=api_key)
    recordings_dir = "./recordings"
    if not os.path.exists(recordings_dir):
        os.makedirs(recordings_dir)

    try:
        response = client.text_to_speech.convert(
            voice_id="AnvlJBAqSLDzEevYr9Ap",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2_5",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = os.path.join(recordings_dir, "ai_output.mp3")
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        print(f"Audio saved to {save_file_path}")
        # play_mp3(save_file_path)
        return save_file_path
    except Exception as e:
        print(f"Error At text_to_speech_file: {e}")
        return None


def simple_pyttsx3_tts(content):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(content)
    engine.runAndWait()
