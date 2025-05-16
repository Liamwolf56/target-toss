import wave
import os

# Create assets folder if it doesn't exist
os.makedirs('assets', exist_ok=True)

def create_silent_wav(path, duration=1, framerate=44100):
    nframes = int(duration * framerate)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)       # mono
        wf.setsampwidth(2)       # 2 bytes per sample (16 bit)
        wf.setframerate(framerate)
        wf.writeframes(b'\x00\x00' * nframes)  # silent audio data

create_silent_wav('assets/throw.wav')
create_silent_wav('assets/hit.wav')

print("Silent placeholder WAV files created in ./assets/")
