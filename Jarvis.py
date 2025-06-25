import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import tkinter as tk
from PIL import Image, ImageTk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except Exception as e:
        print(e)
        print("Sorry, I couldn't understand. Can you please repeat?")
        return "None"
    return query

class JarvisGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Jarvis GUI")

        self.label = tk.Label(self, text=wish_me(), font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.image = Image.open("Tanjiro.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.character_label = tk.Label(self, image=self.photo)
        self.character_label.pack(pady=20)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

if __name__ == "__main__":
    gui = JarvisGUI()
    gui.geometry("400x400")

    gui.mainloop()


