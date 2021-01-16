from gtts import gTTS
from googletrans import Translator
import os

trans = Translator()
text = 'Hello world'
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save('text.mp3')
os.system('start text.mp3')
