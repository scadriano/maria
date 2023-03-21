# Arquivo principal do reconhecimento de fala

# Assistente online!
'''
import speech_recognition as sr

# Criar um reconhecedor de voz
r = sr.Recognizer()

# Abrir o microfone para capturar áudio
with sr.Microphone() as source:
    while True:
        # Definir microfone como fonte de áudio
        audio = r.listen(source)
        print(r.recognize_google(audio, language='pt'))
'''
'''
# Assistente offline!
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
'''

# Assistente offline com Reconhecedor e Síntese de Voz!
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core

# Síntese de voz/fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result =  rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            #speak(text)

            if text == 'que horas são' or 'me diga as horas':
                speak(core.SystemInfo.get_time())