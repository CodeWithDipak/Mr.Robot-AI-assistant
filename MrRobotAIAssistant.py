'''
Author - CodeWithDipak
Date - 9 nov 2020
purpose - Practice Purpose
'''
"""
Mr.Robot AI assistant.
"""


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
dict1 = {
    'mangesh': 'mangeshm760@gmail.com',
    'tejas patil': 'tejasspatil98@gmail.com',
    'sagar kale': 'Sdkale121197@gmail.com',
    'kiran kasar': 'kasarkiran153@gmail.com'
}


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1])
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """This function take an argument audio as a string and speak that string"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This function wish me as good morning,afternoon or evening
    according to time and simply offer a help."""
    hours = int(datetime.datetime.now().hour)
    if 0 <= hours < 12:
        speak("Good morning!")
    elif 12 <= hours < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Mr.Robot. Please tell me how may I help you?")


def takeCommand():
    """It will take microphone input from the user and return as a string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry! I can't recognise your query. Say that again please....")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Enter your email", "Enter your password")
    server.sendmail("Enter your email", to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # Executing the different commands

        if "bye bye" in query:
            speak("Thank you! I am signing off.")
            exit()

        elif "wikipedia" in query:
            try:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", " ")
                search = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia...")
                print(search)
                speak(search)
            except Exception as e:
                print("Page not found!")

        elif "open youtube" in query:
            webbrowser.open_new("youtube.com")

        elif "open google" in query:
            webbrowser.open_new("google.com")

        elif "open stack overflow" in query:
            webbrowser.open_new("stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\Music"
            music = os.listdir(music_dir)
            index = random.randint(0, len(music))
            os.startfile(os.path.join(music_dir, music[index]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "open virtualbox" in query:
            vmBoxPath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(vmBoxPath)

        elif "send email" in query:
            try:
                speak("whom to send the mail?")
                name = takeCommand().lower()
                speak("what should I send?")
                content = takeCommand()
                to = dict1[name]
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry, mail couldn't be send.")
