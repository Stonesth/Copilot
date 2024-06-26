import speech_recognition as sr
from googletrans import Translator
from langdetect import detect
from gtts import gTTS
import os

# create the recognizer object, a translator object
r = sr.Recognizer()
translator = Translator(service_urls=['translate.googleapis.com'])

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

        # translate the text to English
        translated_text = translator.translate(text, dest='en').text

        # convert the translated text to speech
        tts = gTTS(text=translated_text, lang='en')
        tts.save("output.mp3")

        # play the audio file
        os.system("mpg321 output.mp3")
    except Exception as e:
        print(f"Error: {str(e)}")