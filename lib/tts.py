from gtts import gTTS
from random import randint

def generate_speech(text):
    tts = gTTS(text, lang="en")
    file_id = randint(1000, 9999)
    file_name = f'{file_id}.mp3'
    file_path = f'audio/tmp/test_{file_name}'
    tts.save(file_path)
    return file_name