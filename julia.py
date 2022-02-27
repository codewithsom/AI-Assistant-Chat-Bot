import pyttsx3    # pip install pyttsx3
import speech_recognition as sr     # pip install speechRecognition
import datetime
import wikipedia    # pip install wikipedia
import webbrowser 
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Sir    Mam")
        print("Good Morning, Sir/Mam!🙂")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Sir   Mam")
        print("Good Afternoon, Sir/Mam!🙂")
    else:
        speak("Good Evening, Sir Mam")
        print("Good Evening, Sir/Mam!🙂")

    speak("My name is JULIA🤖. How may I assist you?")
    print("My name is JULIA🤖. How may I assist you?")

def takeCommand():
#     # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'play mashup' in query:
            webbrowser.open("https://youtu.be/twfYHXqObcw")

        elif 'play sad song' in query:
            webbrowser.open("https://youtu.be/N_857osuvWw")

        elif 'play english songs' in query:
            webbrowser.open("https://youtu.be/xpVfcZ0ZcFM")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\OneDrive\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir/Mam, the time is {strTime}")
            print(f"Sir/Mam, the time is: {strTime}")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What message should I send?")
                print("What message should I send?")
                content = takeCommand()
                to = "rempire206@gmail.com"
                sendEmail(to, content)
                speak("Your Mail has been sent successfully!")
                print("Your mail has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry buddy. I am not able to send this E-Mail.")
