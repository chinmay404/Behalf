import sounddevice as sd
import numpy as np
import wave
import keyboard
import os

sample_rate = 44100 
channels = 1         
output_dir = "./recordings/"
os.makedirs(output_dir, exist_ok=True)
output_file = "./recordings/output.wav"

def record_audio(output_file=output_file):
    print("Recording... Press SPACE to stop.")
    audio_data = []

    def callback(indata, frames, time, status):
        if status:
            print(f"Warning: {status}")
        audio_data.append(indata.copy())

    with sd.InputStream(samplerate=sample_rate, channels=channels, callback=callback):
        while not keyboard.is_pressed('space'):
            sd.sleep(100) 

    print("Recording stopped.")

    audio_array = np.concatenate(audio_data, axis=0)
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  
        wf.setframerate(sample_rate)
        wf.writeframes((audio_array * 32767).astype(np.int16).tobytes())

    print(f"saved ...")
    return output_file
