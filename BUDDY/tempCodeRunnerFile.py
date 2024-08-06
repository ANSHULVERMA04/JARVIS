import speech_recognition as sr
import pyttsx3     #text to speech

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    # Add your command processing logic here
    pass    

if __name__ == "__main__":
    speak("Initializing Buddy....")
    while True:
        # Listen for the wake word "Buddy"
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "buddy":
                speak("Yes?") # listen for command
                with sr.Microphone() as source:
                    print("Buddy activated...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    
                    processCommand(command)
        
        except Exception as e:
            print("Error: {0}".format(e)) 
