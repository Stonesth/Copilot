import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from langdetect import detect

# create the recognizer object, a translator object, and a text-to-speech object
r = sr.Recognizer()
translator = Translator(service_urls=['translate.googleapis.com'])
tts = pyttsx3.init()

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # listen for audio input from the user
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        input_language = detect(text)
        # translate speech to English if detected language is not English
        if input_language != 'en':
            translation  = translator.translate(text, src=input_language, dest='en')
            print(f"Detected language: {input_language}")
            print(f"Translation: {translation.text}")
            # speak the translated text
            # tts.say(translation.text)
            # tts.runAndWait()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print(f"Error: {e}")



