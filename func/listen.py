import speech_recognition as sr
from .speak import speak

# Initialize the speech recognizer
r = sr.Recognizer()

# Function for listen the input-voice and recognize it
def lisen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        print("Recognizing...")
        command = r.recognize_google_cloud(audio)
    except Exception as e:
        print("Didn't catch that!")
        return ""

    print(command)

lisen()