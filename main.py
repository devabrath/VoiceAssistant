import pyttsx3
import datetime
import wikipedia  # pip install wikipedia
import webbrowser # pip install pyaudio
import os
import pywhatkit
import pyjokes
import smtplib
print("I am your voice assistant")
USER = "Deva"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()



# This funtion will wish you as per the current time
def Greetings():
    hour = int(datetime.datetime.now().hour)
    min=int(datetime.datetime.now().minute)
    print("Time is",hour,":",min)

    if hour >= 0 and hour < 12:
        speak("good morning" + USER)

    elif hour >= 12 and hour < 18:
        speak("good afternoon" + USER)

    else:
        speak("good Evening" + USER)

    speak("i am your assistant. How may I help you?")





# This function will take command from the microphone
def inputVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query


# main program starting
def main():
    speak("Initializing Your voice...")
    Greetings()
    while(True):
        query = inputVoice()
        #command = inputVoice()
        if 'play' in query.lower():
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'youtube' in query.lower():
            webbrowser.open('youtube.com')
            url = "youtube.com"
            chrome_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
            #webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
            webbrowser.open('youtube.com')
            url = "google.com"
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            #webbrowser.get(chrome_path).open(url)
        elif 'joke' in query.lower():
            speak(pyjokes.get_joke())

        elif 'time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{USER} the time is {strTime}")

        elif 'hi'or'hello' in query.lower():
            speak(f"hello {USER}")

        elif 'my name' in query.lower():
            speak(f"your name is {USER}")

main()

