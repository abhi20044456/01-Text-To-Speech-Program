import pyttsx3
engine = pyttsx3.init()

wel = "Welcome to MRX 3.2 speaker"
print(wel)
engine.say(wel)
engine.runAndWait()
while True:
    x = input("What to say?-:")
    if x == "00":
        break
    engine.say(x)
    engine.runAndWait()
Thank = "Thanks to use Speaker MRX 3.2"
print(Thank)
engine.say(Thank)
engine.runAndWait()