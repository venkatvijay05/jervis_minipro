#speech_recognition
import speech_recognition as sr
#AI speeking the voice
import pyttsx3
#Go to the youtube
import pywhatkit

#datetime in current module 
import datetime

#wikipedia module
import wikipedia

#pyjokes in module
import pyjokes 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):   #wikipedia line in multiple line in 2 or 10 line (*text)
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone()  as source:
            print("Listener .......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "jarvis" in command:
                command = command.replace("jarvis","")
                print(command)

    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+ song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time =datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "who the heck is" in command:
        person = command.replace("who the heck is","")
        info = wikipedia.summary(person, 1)  #how many line mention (person,2)
        print(info)
        talk(info)
    elif "are you single" in command:
        talk("I am in  Artificeal intaleginet only realtionship with wifi")

    elif "sholay" in command:
        talk("Solai kumar is a venkat friend, but venkat call me in uncle ")
    elif "joke" in command:
        comedy = pyjokes.get_joke()
        print(comedy)
        talk(comedy)

    else:
        print("Please say the command again.")
        talk("Please say the command again.")
        
while True:        
    run_jarvis()
