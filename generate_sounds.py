import numpy as np
import wave

def generate_beep(filename, duration=0.2, freq=440.0, volume=0.5):
    sample_rate = 44100  # CD-quality audio
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)  # Generate sine wave tone
    tone *= 32767 * volume  # Scale to int16 range and apply volume
    tone = tone.astype(np.int16)

    with wave.open(filename, "w") as f:
        f.setnchannels(1)         # mono
        f.setsampwidth(2)         # 2 bytes per sample (16 bit)
        f.setframerate(sample_rate)
        f.writeframes(tone.tobytes())

# Generate two simple sound files
generate_beep("assets/throw.wav", freq=600)  # a higher-pitched throw sound
generate_beep("assets/hit.wav", freq=300)    # a lower-pitched hit sound

print("Sounds generated!")
