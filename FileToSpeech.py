from gtts import gTTS
import os
file = open("text1.txt", "r").read().replace("\n", " ")
#you can change into any language, I chose Japanese, so my code could speak Jotaro vs DIO battle
language = "ja"
speech = gTTS(text = str(file), lang = language, slow = False)
speech.save("voice.mp3")
os.system("start voice.mp3")