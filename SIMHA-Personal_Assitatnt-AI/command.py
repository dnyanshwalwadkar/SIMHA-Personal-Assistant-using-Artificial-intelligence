import pyttsx3
import pyaudio
import speech_recognition as sr
import  sys, os

def takeCommand():
    #it takes microphone input from usre and returnn string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
         print("Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print("user said:",query)
    except Exception as e:
          print(e)

          print("Say that again ")
          return "None"
    return query  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150) 
engine.setProperty('volume', 0.9)

def speak(audio):
    
    engine.say(audio)
    
    engine.runAndWait()


    