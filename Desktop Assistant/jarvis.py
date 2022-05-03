import pyttsx3  # pyttsx is a cross-platform text to speech library which is platform-independent. The major advantage of using this library for text-to-speech conversion is that it works offline
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib
import subprocess as sp
import keyboard

engine = pyttsx3.init('sapi5')
# It recognize how many types of voice in your pc have
voices = engine.getProperty('voices')
# By this we can check which voice is male or female (0 and 1)

engine.setProperty('voice', voices[1].id)


# Speak Functions ------------------------------
def speak(audio):  # Speak Function
    engine.say(audio)
    engine.runAndWait()  # This function which is used to speak and then wait purpose


# Wish Functions (Using Time date Module) ----------------------------------------------------------------
def wishMe():  # This function is used to wish me through date and time and
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Ayush Sir ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Ayush Sir")
    else:
        speak("Good Evening Ayush sir")

    speak("I am Smart Assistant, Please tell me how may I help you")

# Open and application function ----------------------------------------------------------------


def openApplication():
    speak("Ok sir... ")
    if "code" in query:
        keyboard.press("Ctrl + Alt + V")

    elif "chrome" in query:
        keyboard.press("Ctrl + Alt + C")

    elif "teams" in query:
        keyboard.press("Ctrl + Alt + T")

    elif "My Computer" in query:
        keyboard.press("Ctrl + Alt + E")

# Take Command (using Speech Recognition Module) ----------------------------------------------------------------


def takecommand():  # This function takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        # After completion of speaking words how much it wait for execution
        r.pause_threshold = 0.8
        audio = r.listen(source)
# We used try and catch here because if we can't recognize what user want to say then say none other wise it search in google
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com', 'password')
    server.sendmail('ayushkushwaha261@gmail.com', to, content)
    server.close()


# Main Functions ----------------------------------------------------------------
if __name__ == '__main__':
    wishMe()
    while True:  # By this while function we repetadely Listening after 1 tasks completed.
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open svvv page' in query:
            webbrowser.open("svvv.in")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'code' in query:
            openApplication()

        elif 'play music' in query:
            # music_dir = 'C:\\Users\\ayush\\Music\\MUSIC\\Jarvis songs'
            # By this method we store all songs in songs present in music_dir
            music_dir = 'C:\\Users\\ayush\\Music\\MUSIC\\Jarvis songs\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play songs' in query:

            music_dir = 'C:\\Users\\ayush\\Music\\MUSIC\\Jarvis songs\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play my favourate songs playlist' in query:

            music_dir = 'C:\\Users\\ayush\\Music\\MUSIC\\Jarvis songs\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'how are you' in query:
            speak("Smart assistant always be fine, What's about you ?")

        elif ' I am also fine' in query:
            speak("That's great sir")

        elif 'email to ayush' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = "kushwahaayush261@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent! ")
            except Exception as e:
                print(e)
                speak("Sorry Ayush brother. I am not able to send this email")

        elif 'teams' in query:
            openApplication()

        elif 'chrome' in query:
            openApplication()

        elif 'My computer' in query:
            openApplication()

        elif 'exit Jarvis' in query:
            exit()
