import os, time, subprocess, playsound, random, datetime
import speech_recognition as sr
from gtts import gTTS


def get_audio(source):
    r = sr.Recognizer()

    audio = r.listen(source)
    said = ""

    try:
        said = r.recognize_google(audio)
    except Exception as e:
        print("Exception: " + str(e))

    print(said.lower())
    return said.lower()

def count(words, text):
    count = 0;
    for word in words:
        count += text.count(word)

    return count;

def speak(text):
    aud = gTTS(text=text, lang='en-uk', slow=False)
    aud.save("aud.mp3")
    playsound.playsound('aud.mp3', True)
    os.remove('aud.mp3')

WAKES = ["iris"]
GREETINGS = ['How can I help you?', 'Sir.', 'Here, sir.', 'Nice to see you.', 'Good day, sir.']
QUITS = ["quit", "exit"]
print("Start")
running = True;
woken = False;

while running:
    with sr.Microphone() as source:
        print("Listening")
        text = get_audio(source)

        if count(WAKES, text) > 0:

            # Random Greeting
            if len(text.split()) < 3:
                speak(random.choice(GREETINGS))
            woken = True

        print("Text: " + text)

        # -------------- AlL WOKEN COMMANDS ---------------
        if woken:

            if count(["time"], text) > 0:
                now = datetime.datetime.now()
                time = now.strftime("%H hours and %M minutes")
                speak("It is currently " + str(time))

            if count(SLEEP, text) > 0:
                woken = False


        # ----------------- END COMMANDS --------------------
        # Quit
        if count(QUITS, text) > 0:
            speak("Shutting Down.")
            running = False;
