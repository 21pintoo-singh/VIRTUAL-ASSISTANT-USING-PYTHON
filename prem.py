
import pyttsx3                        # text-to-speech conversion library in Python
import datetime                       # to get time in hours
import speech_recognition as sr       # to take mic input,Speech_recognition is the process of converting spoken words to text. 
import wikipedia                      # to search wikipedia
import webbrowser                     # to open web urls
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine. setProperty("rate", 150)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<4:
        speak('Good night dear Sweet dream')
    elif hour>=4 and hour<12:
        speak('Good Morning Dear Have a good day')
    elif hour>=12 and hour<16:
        speak('Good Afternoon Dear.')
    elif hour>=16 and hour<19:
        speak('Good evening dear.')
    else:
        speak('Good evening dear')
        
    speak('Iam Hazel')
    speak('How can i help you sir')
    
    

def takeCommand():
    # this function takes user command using user mic
    # and it returns output as a string
    # whatever user says
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1     # increase time for 1s. So that it take user voice input even after 1s pause.
            audio = r.listen(source)
    except:
        takeCommand()
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said : {query}\n')
        speak(f'You said :{query}')
    except:
        print('Please say again sir..')
        return "None"
    return query


    
    
    
def wikipediaSearch(query):
    try:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia','')
        print(query)
        results = wikipedia.summary(query, sentences=2)
        speak('According to Wikipedia')
        print(results)
        speak(results)
    except:
        print('Wikipedia not found !')
        
        
        
        
def searchOnGoogle(query):
    query = query.replace('search','')
    query = query.replace('find','')
    webbrowser.open(f'''https://www.google.co.in/search?q={query}&sxsrf=AOaemvLRsASz8xLetx7J7Ofoq7cZfC9llg%3A1639837575890&source=hp&ei=h--9YeeTM7_i2roP_fm26Ac&iflsig=ALs-wAMAAAAAYb39l0oCwzoH43-O2NVNQeSM2QMw5p84&ved=0ahUKEwin88mBx-30AhU_sVYBHf28DX0Q4dUDCAc&uact=5&oq=music&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBwgAELEDEEMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQyQMyBQgAEJIDMgcIABCxAxBDOgcIIxDqAhAnOgQILhAnOgQIABBDOggILhCABBCxAzoFCAAQgAQ6BQgAELEDUL4BWNQJYP8LaAFwAHgAgAHKAYgBhQeSAQUwLjQuMZgBAKABAbABCg&sclient=gws-wiz''')  
    
    
    

    
    
if True:
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            wikipediaSearch(query)
        elif 'close program' in query or 'close the program' in query:
            speak('Thankyou for your time sir')
            speak('Have a nice day')
            break
        elif 'search' in query or 'find' in query:
            searchOnGoogle(query)
     
    
print("Bye")

