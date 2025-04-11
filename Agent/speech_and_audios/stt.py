import os

def get_transcription(filename , client):
    try:
        with open(filename, "rb") as file:
            transcription = client.audio.transcriptions.create(
            file=(filename, file.read()), 
            model="whisper-large-v3",
            prompt="Specify context or spelling",  
            response_format="json", 
            temperature=0.5 
            )
            return transcription.text
    except Exception as e:
        print(f"Error At transcription Groq_Client: {e}")
    