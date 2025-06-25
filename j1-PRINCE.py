import random
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir. I am here to help you")

    def takeCommand():

        r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        random.pause_threshold = 1
        audio = random.listen(source)
# it converts the audio input into string

    try:
        print("Recognizing...")
        query = random.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

    if __name__ == "__main__":

        wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")

        elif "who are you" in query:
            speak("Sir I am Jarvis personal assistant ")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("wikipedia says")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'play music' in query:
            music_dir = "C:\\Users\\Baali\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Baali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using Jarvis Sir")
            exit()
