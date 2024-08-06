import speech_recognition as sr
import webbrowser
import pyttsx3     #text to speech
import musicLibrary     
import requests
import os
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "df4270aec42a4fdd8dc4e867b0b3bd89"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if  "open google"  in c.lower():
        webbrowser.open("https://google.com")
    elif  "open instagram"  in c.lower():
        webbrowser.open("https://instagram.com")
    elif  "open linkedin"  in c.lower():
        webbrowser.open("https://linkedin.com")
    elif  "open youtube"  in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "open x"  in c.lower():
        webbrowser.open("https://x.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
    

        link = musicLibrary.music[song]
        webbrowser.open(link) 
    elif "news" in c.Lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            
            # Extract and print all the titles
            titles = [article['title'] for article in articles if 'title' in article]
            for title in titles:
                speak(title)

             
    else:
         #let open ai handle th request
         pass
                  


if __name__ == "__main__":
    speak("intializing jarvis....")
    while True:
    #Listen for the wake word "jarvis"
    #obtain audio from the microphone
         r= sr.Recognizer()


         print("recognizing...")
         try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=5, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes") #listen for word
                with sr.Microphone() as source:
                      print("jarvis activate..")
                      audio = r.listen(source)
                      command = r.recognize_google(audio)

                      processCommand(command)
    
         except Exception as e:
            print("Error; {0}".format(e))