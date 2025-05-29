from playsound import playsound
import time

audio_files = [
    "Audio/2500.wav",
    "Audio/2000.wav",
    "Audio/1000.wav",
    "Audio/500.wav",
    "Audio/400.wav",
    "Audio/300.wav",
    "Audio/200.wav",
    "Audio/100.wav",
    "Audio/50.wav",
    "Audio/40.wav",
    "Audio/30.wav",
    "Audio/20.wav",
    "Audio/10.wav",
    "Audio/5.wav"
]

for audio in audio_files:
    playsound(audio)
    if "2500" in audio or "2000" in audio or "1000" in audio:
        time.sleep(2)
    elif "500" in audio or "400" in audio or "300" in audio or "200" in audio or "100" in audio:
        time.sleep(1)
    elif "50" in audio or "40" in audio or "30" in audio or "20" in audio or "10" in audio or "5" in audio:
        time.sleep(0.5)

while True:
    playsound("Audio/crc.wav")