import os, time, subprocess, random, datetime, playsound
import speech_recognition as sr
from gtts import gTTS


def get_audio(source):

    return input("() :  ").lower()

    '''
    r = sr.Recognizer()

    audio = r.listen(source)
    said = ""

    try:
        said = r.recognize_google(audio)
    except Exception as e:
        print("Exception: " + str(e))

    print(said.lower())
    return said.lower()
    '''

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


WAKES = ["iris", "cyrus"]
GREETINGS = ['How can I help you?', 'Sir.', 'Here, sir.', 'Nice to see you.', 'Good day, sir.']
QUITS = ["quit", "exit"]
SLEEP = ['sleep', 'thanks', 'thank you']
FILLERS = ['um', 'uh']
print("Start")
running = True;
woken = False;

while running:
    with sr.Microphone() as source:
        text = get_audio(source)

        if count(WAKES, text) > 0:

            # Random Greeting
            if len(text.split()) < 3:
                speak(random.choice(GREETINGS))
            woken = True


        # -------------- AlL WOKEN COMMANDS ---------------
        if woken:

            if count(["time"], text) > 0:
                now = datetime.datetime.now()
                h = int(now.strftime("%H"))
                pm = 'AM'

                if h > 12:
                    pm = 'PM'
                    h -= 12

                time = now.strftime("%H:%M " + pm)
                speak("It is currently " + str(time))

            if count(SLEEP, text) > 0:
                woken = False


        # ----------------- END COMMANDS --------------------
        # Quit
        if count(QUITS, text) > 0:
            speak("Shutting Down.")
            running = False;
