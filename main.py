import os
import time
import speech_recognition as sr
import subprocess


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said.lower())
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def count(words, text):
    count = 0;
    for word in words:
        count += text.count(word)

    return count;


WAKES = ["hello"]
QUITS = ["quit"]
print("Start")
running = True;

while running:
    print("Listening")
    text = get_audio()

    if count(WAKES, text) > 0:
        print("I am ready")
        text = get_audio()
        if count(QUITS, text) > 0:
            running = False;

    if count(QUITS, text) > 0:
        running = False;
