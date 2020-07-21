from gtts import gTTS
import time
from playsound import playsound

while True:
    try:
        msg = input("Meddelande> ")
        language = input("Språk> ")
        fil = input("Slutligt filnamn> ")
        print("\n"*2)

        obj = gTTS(text = msg, lang = language, slow = False)

        obj.save(fil + ".mp3")
    except:
        pass
    playsound(fil + ".mp3")
