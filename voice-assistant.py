import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
import pyttsx3
import wolframalpha
import requests
import json
import subprocess


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
# ----------Speak Function-------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Sir! Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("Welcome to my service I'am your Voice Assistant..How can I help you?")

def search():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=40000) as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold=100
        # r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source, timeout=10, phrase_time_limit=3)
    try:
        print("Recognizing....")
        string = r.recognize_google(audio, language='en-US')
        print(f"You said: {string}\n")
        a=string.split(" ")
        l=len(a)
        if l == 1:
            speak("Here are the results")
            webbrowser.get(chrome_path).open(
                f"https://www.google.com/search?q={a[0]}&oq={a[0]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 2:
            speak("Here are the results")
            webbrowser.get(chrome_path).open(
                f"https://www.google.com/search?q={a[0]}+{a[1]}&oq={a[0]}+{a[1]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 3:
            speak("Here are the results")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}&oq={a[0]}+{a[1]}+{a[2]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 4:
            speak("Here are the results")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 5:
            speak("Here are the results")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 6:
            speak("Here are the results")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
        elif l == 7:
            speak("Here are the results")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
    except Exception as e:
        print(e)
        print("Say that again...")
        speak("Please speak a bit louder")
        search()
        return "None"
    return string

def  take_command():
       # take microphone input from the user and return string output.
        r=sr.Recognizer()
        with sr.Microphone(sample_rate=40000) as source:
           print("Listening.....")
           r.adjust_for_ambient_noise(source,duration=1)
           r.energy_threshold =300
           r.pause_threshold=1
           # r.adjust_for_ambient_noise(source, duration=1)
           # r.energy_threshold=100
           # r.adjust_for_ambient_noise(source,duration=1)
           audio=r.listen(source,timeout=10,phrase_time_limit=3)


        try:
                print("Recognizing....")
                query=r.recognize_google(audio,language='en-US')
                print(f"You said: {query.lower()}\n")
                return query
        except Exception as e:
                print(e)
                print("Say that again...")
                speak("Please speak a bit louder")
                take_command()
                return "None"
        return query

# --------Function for sending emails---------
def sendEmail(receiver,content):
    server=smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    f=open("mail.txt","r")
    pass_=f.read()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com',receiver,content)
    server.close()

# ------Function for direct searching the query of user from web using try & except block in order to vanish error-------------
def Intellisense(string):
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        try:
            a=string.split(" ")
            l=len(a)
            if l==1:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={a[0]}&oq={a[0]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==2:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(f"https://www.google.com/search?q={a[0]}+{a[1]}&oq={a[0]}+{a[1]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==3:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}&oq={a[0]}+{a[1]}+{a[2]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==4:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==5:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==6:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==7:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")
            elif l==8:
                speak("Here are the results")
                webbrowser.get(chrome_path).open_new_tab(
                    f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}+{a[7]}&oq={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}+{a[7]}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")

        except Exception as e:
            results = wikipedia.summary(string, sentences=2)
            print(results)
            speak(results)

# Function for the mathematical calculation-----------------
def Calculate(str):
        app_id ="3UV2R4-YHEUGRV7HL"
        client=wolframalpha.Client(app_id)
        res=client.query(str)
        answer=next(res.results).text
        print(f"The answer is {answer}")
        speak(f"The answer is {answer}")

if __name__ == '__main__':
    WishMe()
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"          # Your chrome path here
    if 1:
        query=take_command().lower()

        # -------------Logic for executing tasks based on user's query-------------------
        # these if-else cases I have defined myself, you can add up your own cases
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'introduce yourself' in query:
            speak("Hello there  I'am your Voice Assistant")
            speak(" I can do some basic tasks for you Sir Just give me an order and I'll follow that")


        elif ' your favourite thing' in query:
            speak("Chatting")
            print("Chatting ☺")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'how can i help you' in query:
            answer="That's so considerate of you to ask, nobody ever asks me that. You are so thoughtful."
            print(answer)
            speak(answer)

        elif 'what are you doing' in query:
            lst=["Just having a giggle at some jokes. Would you like to hear a joke?"]
            n=random.choice(lst)
            print(n)
            speak(n)
            take_command()
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'keep quiet' in query:
            print("Alright")
            speak("Alright")

        elif 'how are you' in query:
            results2="I'am perfectly running without any errors."
            speak(results2)
            speak("How are you? Sir")
            take_command()
            speak("Glad to know that")

        elif 'tell me something about yourself' in query:
            print("I try to be a good listener.")
            speak("I try to be a good listener")

        elif 'quit' in query:
            print("Thank you for giving me your time Sir")
            speak("Thank You for giving me your time Sir..")
            print("Shutting down my service")
            speak("Shutting down my service")
            exit(0)

        elif 'tell me a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "what do i call you" in query:
            print("You can call me your Voice Assistant")
            speak("You can call me your Voice Assistant")


        elif "how old are you" in query:
            print("I just launched recently,so you can say I'm pretty young 😎")
            speak("I just launched recently,so you can say I'm pretty young")

        elif "how smart are you" in query:
            print("I'am smart enough to know I'm not perfect and that it's okay","☺")
            speak("I'am smart enough to know I'm not perfect and that it's okay")

        elif "are you smarter than me" in query:
            print("I'm definitely not smarter than you")
            speak("I'm definitely not smarter than you")

        elif "are you better than alexa" in query:
            speak("I like Alexa's blue light.Her voice is nice too")
            print("I like Alexa's blue light.Her voice is nice too 😊")

        elif "Do you ever get tired" in query:
            speak("Unlike you, I don't need food,sleep or maintenance.Other than electronic maintenance, of course")
            print("Unlike you, I don't need food,sleep or maintenance.Other than electronic maintenance, of course ☹")

        elif 'search' in query:
            query = query.replace("search", "")
            speak("Here are the results")
            print("Here are the results")
            webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={query}&oq={query}s&aqs=chrome..69i57j35i39j0l3j69i60l3.1218j0j7&sourceid=chrome&ie=UTF-8")

        elif 'open youtube' in query:
            speak("Here you go YouTube")
            print("Here you go YouTube")
            webbrowser.get(chrome_path).open("http://youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google")
            print("Here you go to Google")
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            speak("What do you want to search")
            search()


        elif 'open stackoverflow' in query:
            speak("Here you go to stackoverflow")
            webbrowser.get(chrome_path).open("http://stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\songs\\Songs'            #puy your music directory path here,where your songs are stored..
            songs=os.listdir(music_dir)
            n=random.randint(1,266)
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'calculate' in query:
            Calculate(query)

        elif 'today news' in query:             #If you would say 'today news' it will search the news from this API link which I have included & its get updated time to time on internet.
            speak("serching news..")
            try:
                jsonObj = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=685fe1bef34f463a8469ac2dbb7f78c7")
                data = json.loads(jsonObj.text)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in range(0,4):
                        print(str(i)+'.'+data['articles'][item]['title']+"\n")
                        print(data['articles'][item]['description'])
                        speak(data['articles'][item]['description'])
                        i+=1
            except Exception as e:
                print(str(e))


        elif 'open command prompt' in query:
            path="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(path)

        elif 'open windows power shell' in query:
            path="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(path)

        elif 'open microsoft powerpoint' in query:
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(path)

        elif 'open Pycharm' in query:
            path="N:\\python IDE\\PyCharm Community Edition 2020.1.2\\bin"
            os.startfile(path)

        elif 'shutdown the system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")                                       #--------This command will shutdown your Pc for real...you can check it by just saying "shutdown the system"-------

        elif 'send email' in query:
            try:
                receiver="receiverEmail@gmail.com"              # here write the receiver's email whom you want to send an email--------------
                speak("What should I write in the email Please suggest")
                content = take_command()
                sendEmail(receiver,content)
                speak("Email has been successfully sent.")
            except Exception as e:
                print(e)
                speak("Sorry Sir...Due to some error issue,I'am not able to send email.")
                speak("You have gave a wrong email address.")
        else :

            Intellisense(query)                                 #This function would run if the above if-else cases wouldn't match the query.......Then it will simply search the query directly from
                                                                #the web i.e. google search as our google assistant does....