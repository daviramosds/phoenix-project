from gtts import gTTS
from random import randint
from os import getenv, remove
import base64


def generate_speech(text):
    tts = gTTS(text, lang="en")
    file_id = randint(1000, 9999)
    TMP_FILE_PATH = getenv('TMP_FILE_PATH')
    AUDIO_FILE_PREFIX = getenv('AUDIO_FILE_PREFIX')
    file_name = f'{file_id}.mp3'
    file_path = f'{TMP_FILE_PATH}{AUDIO_FILE_PREFIX}{file_name}'
    tts.save(file_path)


    with open(file_path, "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read())
        
    remove(file_path)
    
    encoded_string = str(encoded_string)
    encoded_string = encoded_string.replace("b'", '')
    encoded_string = encoded_string.replace("'", '')

    return str(encoded_string)
