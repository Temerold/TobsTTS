try:
    from gtts import gTTS
    import time
    from playsound import playsound
    from tkinter import *
except ImportError:
    pass



# tags
version = "0.0 lel" # version
copyright_ = "Tob's TTS is brought to you by Temerold.se " # copyright_


# window
window = Tk()
window.title("Tob's TTS | " + version)
window.geometry("780x580")
window.configure(background = "black")

window.resizable(False, False)

copyright_lbl = Label(window, text = copyright_) # and deserved
copyright_lbl.place(x = 0, y = 560)

ms = Entry(window, width = 24)
ms.place(x = 540, y = 135)

text = Label(window, text = "Text", anchor = "e")
text.place(x = 505, y = 135)



fi = Entry(window, width = 24)
fi.place(x = 540, y = 165)

slut = Label(window, text = "Slutlig fil", anchor = "e")
slut.place(x = 481, y = 165)



def clicked():
    msg = ms.get()
    language = "sv"
    fil = fi.get()
    obj = gTTS(text = msg, lang = language, slow = False)

    obj.save(fil + ".mp3")
    playsound(fil + ".mp3")

def click2():
    msg = ms.get()
    language = "en"
    fil = fi.get()
    obj = gTTS(text = msg, lang = language, slow = False)

    obj.save(fil + ".mp3")
    playsound(fil + ".mp3")

    
btn = Button(window, text = "Skapa", width = 17, font = ("", 10), command = clicked)
btn.place(x = 541, y = 105)

def toggle():
    global btn
    global t_btn
    global language
    
    if t_btn.config("text")[-1] == "Engelska":
        t_btn.config(text="Svenska")
        btn.config(command = clicked)
    else:
        t_btn.config(text="Engelska")
        btn.config(command = click2)

t_btn = Button(window, text = "Svenska", width = 17, font = ("", 10), command = toggle)
t_btn.place(x = 541, y = 75)

window.mainloop()
