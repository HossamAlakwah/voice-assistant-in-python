#name:hossam mohamed alakwah
#id:20191094
import pyttsx3
import speech_recognition as sr
import random
import weather
import web
from youtube import *
import youtube
from news import *
import randfacts
from joke import *
from weather import *
import datetime




speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')

                    #Asking the user which voice he prefere
#speaker.say("press 0 for male , 1 for female")
#speaker.runAndWait()


flag_4 = False


def speak(text):
    speaker.say(text)
    speaker.runAndWait()
r = sr.Recognizer()


r_1 = sr.Recognizer()
mic_1 = sr.Microphone()

with mic_1 as source:
    #spectrum of our voice (even low voices)
    r_1.energy_threshold = 10000
    #cancel all the noises around us
    r_1.adjust_for_ambient_noise(source, 1.2)
    print("which voice do you like:- male or female")
    speak("which voice do you like," + " male or female")
    print("Listenning...")
    audio = r_1.listen(source)
    vo = r_1.recognize_google(audio)
    try:

        if (vo == "male"):
            speaker.setProperty('voice', voices[0].id)
            speak("ok, male is speaking")


        elif (vo == "female"):
            speaker.setProperty('voice', voices[1].id)
            speak("ok, female is speaking")

        else:
            print("sorry, i couldn't do this the default voice is applied")
            speak("sorry, i couldn't do this. the default voice is applied")
        print(vo)
        time.sleep(2)

    except sr.UnknownValueError:
        print("sorry i did't get that")
        speak("sorry i did't get that")
        vo="female"
    except sr.RequestError:
        print("sorry my service is down now")
        speak("sorry my service is down now")
        vo="female"




def firsttalk():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return ("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")
print("hello hossam, good "+firsttalk()+ ", Iam your voice assistant")
speak("hello hossam, good "+firsttalk()+ ", Iam your voice assistant")

mic = sr.Microphone()

with mic as source:
    #spectrum of our voice (even low voices)
    r.energy_threshold = 10000
    #cancel all the noises around us
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listenning...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)

    except sr.UnknownValueError:
        print("sorry i did't get that")
        speak("sorry i did't get that")
        vo="male"
    except sr.RequestError:
        print("sorry my service is down now")
        speak("sorry my service is down now")

condition = ["how are you", "what about you", "what is going on", "what's up", "how is everything", "you all right","how is your day going"]
condition_rep = ["Iam fine Thank you, I appreciate you looking into this matter", "I’m doing fine", "I’m doing good", "I’m feeling just fine", "I’m okay"]

for i in range(0, 7):
    if text.__contains__(condition[i]):
        responde = random.choice(condition_rep)
        print(responde)
        speak(responde)
        break
else:
    try:
        print("You said: ", r.recognize_google(audio))
    except sr.UnknownValueError:
        speak("Could not understand audio")
    except sr.RequestError as e:
        speak("Could not request results; {0}".format(e))
    speak("I don't have reply for this")




still_running = True
while still_running:
    with mic as source:
        # spectrum of our voice (even low voices)
        r.energy_threshold = 10000
        # cancel all the noises around us
        r.adjust_for_ambient_noise(source, 1.2)
        print("what can i do for you??")
        speak("what can i do for you??")

        print("Listenning...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
    # if text2 == 'bye bye' or text2 == 'nothing' or 'good bye':
    #     still_running = False
    #     exit()
    # else:
    #     pass


    # print(text2)


    #infoo=["wikipedia", "information", "knowledge", "info"]
    #youtube_list=["YouTube", "play video","video clip"]
    #news_list=["news","latest news"]
    #fact_list=["true","fact"]
    again=["here we go again", " here is another fact", "ok take this one"]
    #joke_list=["tell me a joke","tell me a joke","funny short story", "witticism", "jest"]
    #weather_list=["weather", "weather summary"]
    f_1=False
    for j in range(0, 4):
        if text2.__contains__(infoo[j]) :
            f_1=True
            print('you need to search for which topic?')
            speak('you need to search for which topic?')
            with mic as source:
            # spectrum of our voice (even low voices)
                r.energy_threshold = 10000
            # cancel all the noises around us
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listenning...")
                audio = r.listen(source)
                inf = r.recognize_google(audio)
            print("Searching for {} in wikipedia".format(inf))
            speak("Searching for {} in wikipedia".format(inf))
            web.info().get_info(inf)
            time.sleep(5)
            break
        pass

        # elif j==4:
        #     try:
        #         print("You said: ", r.recognize_google(audio))
        #     except sr.UnknownValueError:
        #         speak("Could not understand audio")
        #     except sr.RequestError as e:
        #         speak("Could not request results; {0}".format(e))
    f_2=False
    for j in range(0, 3):
        if text2.__contains__(youtube_list[j]):
            f_2=True
            print("which video you want me to play??")
            speak("which video you want me to play??")
            with mic as source:
            # spectrum of our voice (even low voices)
                r.energy_threshold = 10000
            # cancel all the noises around us
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listenning...")
                audio = r.listen(source)
                vid = r.recognize_google(audio)
            print("Searching for {} in youtube".format(vid))
            speak("playing for {} in youtube".format(vid))
            youtube.play().play_video(vid)

            time.sleep(5)
            break

    f_3=False
    for j in range(0, 2):
        if text2.__contains__(news_list[j]):
            f_3 = True
            print("here is the latest news!")
            speak("here is the latest news!")
            time.sleep(3)
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
            break
        elif text2.__contains__(fact_list[j]):
            f_3=True
            rep_fact=["did you know that", "had you any idea that","could you even have imagined that"]
            print("number of facts you want to listen for: ")
            speak("please enter number of facts you want to listen for:")
            no=input()
            no = int(no)
            if no==0:
                break
            elif no==1:
                random_fact = randfacts.get_fact()
                print("fact" + ": "+random.choice(rep_fact)+" " + random_fact)
                speak(random.choice(rep_fact) + random_fact)
                time.sleep(2)
                flag_4=True
                while flag_4:
                    print("if it was exciting and you want one more fact press 'y' ")
                    speak("if it was exciting and you want one more fact press 'y' ")
                    another=input()

                    if another=="y":
                        x=randfacts.get_fact()
                        y=random.choice(again)
                        print("fact: "+y+" " + x)
                        speak(y + x)
                    else:
                        flag_4=False
                        break
                break
            else:
                for i in range(no):
                    random_fact=randfacts.get_fact()
                    ff="fact " + str(i+1) +": "+ random_fact
                    print(ff)
                    speak(ff)
                break

        elif text2.__contains__(weather_list[j]):
            f_3=True
            print("enter the city you want to know it's weather summary:- ")
            speak("enter the city you want to know it's weather summary:- ")
            cc=input()
            test_weather = weather.take_city(cc)
            speak(str(take_city(cc)))
            time.sleep(5)
            break

    f_4=False
    for j in range(0, 5):
        if text2.__contains__(joke_list[j]):
            ar=joke()
            f_4 = True
            print("here is a joke!")
            speak("here is a joke!")
            time.sleep(1)
            print(ar[0])
            speak(ar[0])
            time.sleep(1)
            print(ar[1])
            speak(ar[1])
            time.sleep(1)
            ask_joke=["wasn't is funny?!","was it a good joke?!"]
            lo=random.choice(ask_joke)
            print(lo)
            speak(lo)
            time.sleep(0.5)
            time.sleep(5)
            break
        if text2 == "go to sleep" or text2 == "bye":
            still_running=False
            print("ok, i hope i helped you")
            speak("ok, i hope i helped you")
            break

        if f_1 == False and f_2 == False and f_3 == False  and f_4==False :
            try:
                print("i can't do that for you")
                speak("i can't do that for you")
                break
            except sr.UnknownValueError:
                speak("Could not understand you")
                break
            except sr.RequestError as e:
                speak("Could not request results; {0}".format(e))
                break

            speak("I don't have reply for this")







