import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import noisereduce as nr

duration = 20  # Augmentez la durée pour capturer un segment audio plus long
base_filename = "/Users/thononpierre/Documents/Projet/Python/Project/Copilot/recorded_audio"
file_counter = 1

sample_rate = 48000  # Augmentez le taux d'échantillonnage pour une meilleure qualité
channels = 1  # Enregistrement mono

for _ in range(4):
    print("Enregistrement en cours...")

    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()

    reduced_noise = nr.reduce_noise(y=recording[:, 0], sr=sample_rate)

    filename = f"{base_filename}_{file_counter}.wav"
    sf.write(filename, reduced_noise, sample_rate)

    print(f"Enregistrement enregistré sous {filename}")

    r = sr.Recognizer()
    audio_file = sr.AudioFile(filename)

    try:
        with audio_file as source:
            audio = r.record(source)

        text = r.recognize_google(audio)

        print("Transcription:")
        print(text)

    except sr.UnknownValueError:
        print("Impossible de transcrire l'audio. Aucun texte détecté.")

    except sr.RequestError as e:
        print("Une erreur s'est produite lors de la demande du service de reconnaissance vocale: {0}".format(e))

    file_counter += 1
