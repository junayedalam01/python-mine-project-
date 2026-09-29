import pyttsx3
import time

speech =pyttsx3.init()
time.sleep(3)
for i in range(1,50):
    v= str(i)
    print(v)
    speech.say(v)
    speech.runAndWait()

    time.sleep(1)

