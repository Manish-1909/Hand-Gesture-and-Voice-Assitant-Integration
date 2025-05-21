import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
from datetime import date
import wikipedia # pip install wikipedia
import webbrowser
from threading import Thread
import gesture_controller

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
today = date.today()

# Function to speak out the provided text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Manish!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Manish!")   
    else:
        speak("Good Evening Manish!")  
    speak("I am Spartan. Please tell me how may I help you")       

# Function to take voice commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "hello" in query:
            wishMe()

        elif 'what is your name' in query:
            speak('My name is Spartan!')

        elif 'todays date' in query:
            tdate=today.strftime("%B %d, %Y")
            speak(f"Sir, the time is {tdate}")
            
            

        elif 'search' in query:
            speak('Searching for ' + query.split('search')[1])
            url = 'https://google.com/search?q=' + query.split('search')[1]
            try:
                webbrowser.get().open(url)
                speak('This is what I found Sir')
            except:
                speak('Please check your Internet')

        elif 'location' in query:
            speak('Which place are you looking for?')
            temp_audio = takeCommand()
            speak('Locating...')
            url = 'https://google.nl/maps/place/' + temp_audio
            try:
                webbrowser.get().open(url)
                speak('This is what I found Sir')
            except:
                speak('Please check your Internet')
            
        elif ('launch gesture controller' in query) or ('open gesture controller'in query):
            if gesture_controller.GestureController.gc_mode:
                speak('Gesture controller is already active')
            else:
                gc = gesture_controller.GestureController()
                t = Thread(target = gc.start)
                t.start()
                speak('Launched Successfully')
        elif ('stop gesture controller' in query) or ('close gesture controller' in query):
            if gesture_controller.GestureController.gc_mode:
                gesture_controller.GestureController.gc_mode = 0
                speak('Gesture recognition stopped')
            else:
                speak('Gesture controller is already inactive')
                
        elif ('exit' in query) or ('terminate' in query):
            if gesture_controller.GestureController.gc_mode:
                gesture_controller.GestureController.gc_mode = 0
            break
            



    speak("Exiting the system")