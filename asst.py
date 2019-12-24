
"""
pip install speech_recognition
pip install webbrowser
pip install pyttsx3
pip install wikipedia

"""
import speech_recognition as sprc
import webbrowser as w
import pyttsx3 as pts
import wikipedia as wik

sprc.Microphone(device_index=1)
r=sprc.Recognizer()
r.energy_threshold=6000

au=pts.init()
au.setProperty("voice",au.getProperty("voices")[1].id)
au.setProperty("rate",200)
au.setProperty("volume",0.9)
s=""
def speak(audi):
    au.say(audi)
    au.runAndWait()

def cmd():
    with sprc.Microphone() as src:
        iau=r.listen(src)
        try:
            s=r.recognize_google(iau,language="en-in")
            print("you said {}".format(s))
            speak("you said "+s)
        except:
            print("cant recognize say again...")
            speak("cant recognize say again...")
            s=cmd()
   # s="search google for time "
    return s
print("getting started \nthis is python assistant how can I help you ")
speak("this is python assistant how can I help you ")
print("say something")
speak("say something")

def srh():
    st=cmd()
    print("1.Google\n2.Wikipedia\n3.youtube")
    speak("say Google or Wikipedia or youtube")
    ct=cmd()
    print(ct)
    if "Google" in ct:
    #if(False):
        m=st
        print("you searched for "+m)
        sqr="https://www.google.co.in/search?q="
        speak("searching in google")
        w.open(sqr+m)
    elif "Wikipedia" in ct:
        try:
            rs=wik.page(st).content
            speak("searching in wikipedia")
            print(rs)
            print("do you want to know more click on it")
            speak("do you want to know more click on it")
            rs=wik.summary(st,sentences=4)
            print(rs)
            speak(rs)
        except:
            print("wikipedia does have the info about your search soryy")
            speak("wikipedia does have the info about your search soryy")
    elif "YouTube" in ct:
        m=st
        sqr="https://www.youtube.com/results?search_query="
        speak("searching in youtube")
        w.open(sqr+m)
    else:
        print("invalid option choosen plzz say it again")
def main():
    print("say\n1.search\n2.what is the time now\n3.who am I\n4.calculator")
    speak("select the above options")
    st=cmd()
    if "Search"==st:
        srh()
    elif ""
    else:
        print("invaild option say again")
        speak("invaild option say again")
        main()
main()

