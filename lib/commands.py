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


def exec(cmd):
    if 'google search' in cmd:
        cmd = cmd.split('google search')
        term = cmd[1].strip()
        if 'about' in term.split(' ')[0]:
            term = term.replace('about', '')
        message = f'google searching {term}'
        google_search(term)
        audio_b64 = tts.generate_speech(message)
        return jsonify({'message': message, 'audio_b64': audio_b64})

    if 'show my devices' in cmd:
        cmd = 'find my devices'
        message = f'showing your devices'
        show_my_devices()
        audio_b64 = tts.generate_speech(message)
        return jsonify({'message': message, 'audio_b64': audio_b64})

    if 'test' in cmd:
        print('TEST COMMAND')
        return jsonify({'message': 'test command'})
    else:
        return jsonify({'message': 'invalid command'})
