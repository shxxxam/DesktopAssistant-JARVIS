import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import os 
import smtplib 
import random
from requests import get
import pywhatkit as kit 
import sys

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
# print(voices[1],id) #shows the voices present in your device
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''
    This function will pronounce the string which is passsed to it 
    '''
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.


def WishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Initializing Jarvis.... ")
    if hour >= 0 and hour <12:
        speak("Good Morning!")
    
    elif hour >=12 and hour <18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")

    
    speak("Please tell me how may I help you?")

def takecommand():
    '''
    This function takes microphone input from the user and returns string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening.....")
        r.energy_threshold = 290
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio) 
        print(f"User said: {query}\n") #User's query will be printed

    except Exception as e:
        print(e) # Prints the error
        print("Say that again please...") # also be printed in case of improper voice
        query = "Nothing"
    return query 

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('EmailID@gmail.com','Password')
    server.sendmail('EmailID@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google search' in query:
            speak('Sir, What should I search on google?')
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            code_path = "C:\\Users\std11\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif "email to Reciever's name" in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = "Reciever'sEmailID@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Master!, I am not able to send this email") 
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\std11\\Music\\All"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            # for song in songs:   #use to play only mp3 files
            #     if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir, rd))

        elif 'my ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"your IP address is {ip}\n")
            speak(f"your IP address is {ip}\n")

        elif 'youtube search' in query:
                speak('What do you want to search?')
                sg = takecommand().lower()
                kit.playonyt(sg)

        elif 'thank you' in query:
            speak("you're welcome")

        elif 'no thanks' in query:
            speak("Thanks for using me, have a great day sir!")
            sys.exit()


        speak('Sir, any other work?') 