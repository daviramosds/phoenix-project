from gtts import gTTS
from random import randint
from os import getenv

def generate_speech(text):
    tts = gTTS(text, lang="en")
    file_id = randint(1000, 9999)
    AF_PATH = getenv('TMP_FILE_PATH')
    AF_PREFIX = getenv('AUDIO_FILE_PREFIX')
    file_name = f'{file_id}.mp3'
    file_path = f'{AF_PATH}{AF_PREFIX}{file_name}'
    tts.save(file_path)
    return file_name