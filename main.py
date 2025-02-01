import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from gtts import gTTS
import base64
import tempfile

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_audio(audio_path):
    # Placeholder for any additional processing
    return "Processed text from audio file."


def generate_audio_response_base64(text):
    """Generate audio response from text and return as base64."""
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as temp_audio:
        tts.save(temp_audio.name)
        with open(temp_audio.name, "rb") as audio_file:
            return base64.b64encode(audio_file.read()).decode('utf-8')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process-audio', methods=['POST'])
def process_audio_request():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    file = request.files['audio']
    print(file)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Simulate processing the uploaded audio file
        processed_text = process_audio(file_path)

        # Generate a TTS audio response and encode it as base64
        audio_base64 = generate_audio_response_base64("Your message has been processed.")

        return jsonify({
            'message': "Audio processed successfully.",
            'processed_text': processed_text,
            'audio_base64': audio_base64
        })
    else:
        return jsonify({"error": "Invalid file type. Only wav, mp3, and m4a are allowed."}), 400


@app.route('/play-audio', methods=['POST'])
def play_audio_request():
    """Endpoint to generate and send audio encoded as base64."""
    data = request.json
    text = data.get("text", "No text provided.")
    audio_base64 = generate_audio_response_base64(text)
    return jsonify({"audio_base64": audio_base64})


if __name__ == '__main__':
    app.run(debug=True)
