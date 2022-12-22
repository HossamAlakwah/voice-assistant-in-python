import sre_constants

from main import *
def record_audio():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, i did not get that")
        except sr.RequestError:
            print('sorrry, mu speech service is down')
        return voice_data