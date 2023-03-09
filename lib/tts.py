from gtts import gTTS
from os import getenv, remove, path, system
import base64
from pydub import AudioSegment

def change_speed(audio_file_path): 
    # change audio speed
    sound = AudioSegment.from_file(audio_file_path, format="mp3")
    sound = sound.speedup(playback_speed=1.2)
    sound.export(audio_file_path, format="mp3")

def generate_speech(text):
    
    TMP_FILE_PATH = getenv('TMP_FILE_PATH')
    CACHE_FILE_PATH = getenv('CACHE_FILE_PATH')
    AUDIO_FILE_PREFIX = getenv('AUDIO_FILE_PREFIX')
    slug = text.lower().strip().replace(' ', '_')
    audio_file_path = f'{TMP_FILE_PATH}{AUDIO_FILE_PREFIX}{slug}.mp3'
    cache_file_path = f'{CACHE_FILE_PATH}{AUDIO_FILE_PREFIX}{slug}.b64'

    if path.isfile(cache_file_path):
        print('already exist')
        f = open(cache_file_path, 'r')
        return f.read().replace("b'", '')
    else:
        tts = gTTS(text, lang="en")

        tts.save(audio_file_path)
        change_speed(audio_file_path)

        with open(audio_file_path, "rb") as audio_file:
            encoded_string = str(base64.b64encode(audio_file.read())).replace("b'", '').replace("'", '')

        remove(audio_file_path)

        system(f'echo {encoded_string} > {cache_file_path}')

        return encoded_string