import pyttsx3  
import datetime  
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  
import pyautogui
import psutil 
import pyjokes  
import requests, json 

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)


#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")


#welcome function
def wishme():
    speak("Welcome Back Sir")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Allow me to introduce myself,I am Jarvis, the virtual artificial intelligence,and I'm here to assist you with a variety of tasks, 24 hours a day seven days a week.")
    speak("What would you like to do today")


def wishme_end():
    speak("Initiating program quit operation,Quitting program")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Have a nice day Sir")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon Sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening Sir")
    else:
        speak("Goodnight Sir.. Sweet dreams")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


#sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("user-name@xyz.com", "pwd")
    server.sendmail("user-name@xyz.com", to, content)
    server.close()


#screenshot function
# def screenshot():
#     img = pyautogui.screenshot()
#     img.save(r'path to folder in which you would like to save screenshot')


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent)
    )



#weather condition
def weather():
    api_key = "YOUR-API_KEY" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    speak(
        "I am Jarvis, version 3.0, I am a voice assistent, developed by Your_name  team on 25 December 2022 in INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()
        

        
#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching ...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#sending email

        # elif ("send email" in query):
        #     try:
        #         speak("What is the message for the email")
        #         content = takeCommand()
        #         to = 'reciever@xyz.com'
        #         sendEmail(to, content)
        #         speak("Email has sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Unable to send email at the moment")


        elif 'open youtube' in query:
            speak("opening youtube ")
            wb.open("youtube.com")

        elif 'open google' in query:
            speak("opening google ")
            wb.open("google.com")

        elif 'openstack' in query:
            speak("opening stackoverflow ")
            wb.open("stackoverflow.com") 

        elif 'open flipkart' in query:
            speak("opening flipkart ")
            wb.open("flipkart.com")     

        elif 'changes' in query:
            speak("opening visual studio")
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    

#system logout/ shut down 

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            speak(" Initiating  system restart")
            speak("restarting")
            os.system("shutdown /r /t 1")
        elif ("shut down" in query ):
            speak("Initiating  system Shutdown process")
            speak("Process complete,Shutting down")
            os.system("shutdown /r /t 1")

        elif 'play music' in query:
            speak("Playing")
            music_dir = r'path to your music folder'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))   #songs[1]
            #quit()

#reminder function

        elif ("add  reminder" in query or "reminder" in query):
            speak("What is the reminder Sir?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open(r"path to destination folder", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open(r"path to destination folder", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        # elif ("screenshot" in query):
        #     speak("Taking screenshot")
        #     screenshot()
        #     speak("Done!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()


#weather
        elif ("weather" in query or "temperature" in query):
            weather()

#jarvis features
        elif ("you do" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can open websites,
            i can search on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            now you know my features,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)

        elif ("male" in query or "female" in query):
            if ("female" in query):
                speak("Changing voice to female voice")
                voice_change(1)
            elif ("male" in query):
                speak("Changing voice to male voice")
                voice_change(0)

#exit function

        elif ('i am done' in query or 'bye bye jarvis' in query
              or 'go offline jarvis' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()