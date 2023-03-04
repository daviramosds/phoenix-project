import webbrowser
from urllib import parse
from flask import jsonify
from lib import tts

def test():
    print('test command')

def google_search(text):  # say google search {search}
    web_encode = parse.quote(text)
    webbrowser.open(f"https://www.google.com/search?q={web_encode}")
    print(f'google searching {text}')

def exec(cmd):
    if 'google search' in cmd:
        cmd = cmd.split('google search')
        term = cmd[1].strip()
        audio = tts.generate_speech(f'google searching {term}')
        print(audio)
        google_search(term)

        return jsonify({ 'message': f'google searching {term}' })
    if 'test' in cmd:
        print('TEST COMMAND')
        return jsonify({ 'message': 'test command' })
    else:
        return jsonify({ 'message': 'invalid command' })
