import sounddevice as sd
import numpy as np
import speech_recognition as sr
from langdetect import detect
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from langdetect import detect
from tqdm import tqdm

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Parlez maintenant...")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    
    try:
        text = r.recognize_google(audio)
        input_language = detect(text)
        print(f"Langue détectée : {input_language}")
        
        transcription = r.recognize_google(audio, language='fr-FR')
        print("Transcription : " + transcription)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))