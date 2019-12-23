import speech_recognition as sprc
import webbrowser as w
import pyttsx3 as pts
import wikipedia as wik

sprc.Microphone(device_index=1)
r=sprc.Recognizer()
r.energy_threshold=4500

au=pts.init()
au.setProperty("voice",au.getProperty("voices")[1].id)
au.setProperty("rate",200)
au.setProperty("volume",0.9)
s=""
def speak(audi):
    au.say(audi)
    au.runAndWait()

def cmd():
    print("say something")
    speak("say something")
    with sprc.Microphone() as src:
        iau=r.listen(src)
        try:
            s=r.recognize_google(iau,language="en-in")
            print("you said {}".format(s))
            speak(s)
        except:
            print("cant recognize say again...")
            cmd()
   # s="search google for time "
    return s
print("getting started")
speak("this is python assistant how can I help you ")
def main():
    st=cmd()
    if "search Google for" or "what is " in st:
            m=st[(st.index("search Google for")+len("search google for")):len(st)]
            print("you searched for "+m)
            sqr="https://www.google.co.in/search?q="
            w.open(sqr+m)
    else:
        main()
main()

