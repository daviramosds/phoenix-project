import webbrowser
from urllib import parse
from flask import jsonify
from lib import tts

def test():
    print('test command')

def google_search(text):  # say google search {search}
    web_encode = parse.quote(text)
    webbrowser.open(f'https://www.google.com/search?q={web_encode}')

def show_my_devices():
    webbrowser.open('https://www.google.com/android/find/')

def respond(text):
    audio_b64 = tts.generate_speech(text)
    return jsonify({'message': 'invalid command', 'audio_b64': audio_b64})

def exec(cmd):
    if 'google search' in cmd:
        cmd = cmd.split('google search')
        print(cmd)
        term = cmd[1].strip()
        if 'about' in term.split(' ')[0]:
            term = term.replace('about', '')
        google_search(term)
        return respond(f'google searching {term}')

    if 'show my devices' in cmd:
        show_my_devices()
        return respond('showing your devices')

    if 'test' in cmd:
        return respond('TEST COMMAND')

    if 'generate speech' in cmd:
        return respond('Hello master! what can i do for you?')

    if 'thanks' in cmd or 'thank you' in cmd:
        return respond("You're Welcome")

    else:
        return respond('invalid command')
