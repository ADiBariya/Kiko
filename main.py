from wake_word import listen_for_wake_word
from speech_to_text import transcribe_audio
from ai_response import get_response
from tts import speak
from elevenlabs import play
from elevenlabs.client import ElevenLabs

def main():
    print("🟢 Kiko is active. Say 'Kiko' to talk...")
    while True:
        if listen_for_wake_word():
            speak("Yes, Adi?")
            user_input = transcribe_audio()
            print(f"You said: {user_input}")
            reply = get_response(user_input)
            print(f"Kiko: {reply}")
            speak(reply)

if __name__ == "__main__":
    main()
# Main file to run Kiko AI
