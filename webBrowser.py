# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:37:27 2023

@author: AzuDevCR
"""

import webbrowser
import time
import speech_recognition as sr

def deviceList():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f'Microphone with name {name} found for Microphone(device_index={index})')

speech = sr.Recognizer()
def voiceToText(): #Non-Pythonic sintax justCause
    sr.Microphone(device_index = 10)
    voiceInput = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voiceInput = speech.recognize_google(audio)
        except sr.UnknownValueError:
            print("Can't understand you... Please try again")
            pass
        except sr.RequestError:
            print("Service offline... Please try again")
            pass
        except sr.WaitTimeoutError:
            print("Can't hear you... Please try again")
            pass
    return voiceInput

while True:
    time.sleep(2.5)
    print("Python is listening...")
    inp = voiceToText()
    print(f'You just say {inp}.')
    if inp == "stop":
        print("Goodbye!")
        break
    elif "browser" in inp:
        inp = inp.replace('browser ', '')
        webbrowser.open("http://google.com/search?q="+inp)
        continue
