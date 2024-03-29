# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:19:21 2020

@author: Azeemushan
"""

import speech_recognition as sr #pip install speechRecognition

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        #print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    print("You Said- ",str(query))
    return query


cmd = takeCommand()