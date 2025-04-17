from elevenlabs import ElevenLabs, VoiceSettings
import simpleaudio as sa

client = ElevenLabs(api_key="sk_f6bc50703251e63d2885eb1de688d64bd9063dce850aaf14")

def speak(text):
    audio = client.generate(
        text=text,
        voice="Rachael",
        model="eleven_multilingual_v2",
        stream=False  # stream=False gives you full audio bytes
    )
    
    # Play audio using simpleaudio
    play_obj = sa.play_buffer(audio, 1, 2, 22050)  # mono, 16-bit, 22.05kHz
    play_obj.wait_done()