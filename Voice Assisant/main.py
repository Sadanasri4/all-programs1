import pyttsx3 as p

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
print(rate)
engine.say("hell world . my name is nova")
engine.runAndWait()