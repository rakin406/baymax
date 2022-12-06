#!/usr/bin/env python3
"""
This is an Artificial Intelligence voice-bot which communicates with people.
Usage: ./baymax.py
"""

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()
print("Press Ctrl-c to stop program")


def speak(text: str):
    engine.say(text)
    engine.runAndWait()


engine.setProperty("rate", 130)  # set up voice rate
speak("Hello, I am Baymax, your personal healthcare companion.")


# Recognize speech using Sphinx
while True:
    try:
        # FIX: Microphone detection issues. ALSA lib unable to open slave.
        with sr.Microphone() as source:
            audio = r.listen(source)
            speak(r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        break
