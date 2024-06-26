import speech_recognition as sr
from googletrans import Translator

# Créer un objet de reconnaissance vocale
r = sr.Recognizer()

# Utiliser le microphone comme source audio
with sr.Microphone() as source:
    print("Dites quelque chose...")
    audio = r.listen(source)

try:
    # Reconnaître le texte à partir de l'audio
    text = r.recognize_google(audio, language='fr-FR')
    print("Texte reconnu : " + text)

    # Traduire le texte en anglais
    translator = Translator()
    translation = translator.translate(text, dest='en')
    print("Traduction en anglais : " + translation.text)

except sr.UnknownValueError:
    print("Impossible de reconnaître le texte.")
except sr.RequestError as e:
    print("Erreur lors de la requête : {0}".format(e))