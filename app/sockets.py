from flask_socketio import emit
import base64
# from .audio_processing import process_audio

def register_sockets(socketio):
    @socketio.on("audio")
    def handle_audio(data):
        """Receive, process, and return audio."""
        try:
            audio_data = base64.b64decode(data)
            processed_audio = process_audio(audio_data)
            encoded_audio = base64.b64encode(processed_audio).decode("utf-8")
            emit("audio_response", encoded_audio)
        except Exception as e:
            print(f"Error processing audio: {e}")
