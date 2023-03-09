import webbrowser
from urllib import parse
from flask import jsonify
from lib import tts
from os import system
import subprocess
import pyautogui

def test():
    print('test command')

def google_search(text):  # say google search {search}
    web_encode = parse.quote(text)
    subprocess.Popen(f'/opt/brave.com/brave/brave --app=https://www.google.com/search?q={web_encode}', shell=True)
    # webbrowser.open(f'https://www.google.com/search?q={web_encode}')

def show_my_devices():
    subprocess.Popen('/opt/brave.com/brave/brave --app=https://www.google.com/android/find/', shell=True)
    # webbrowser.open('https://www.google.com/android/find/')

def respond(text):
    audio_b64 = tts.generate_speech(text)
    return jsonify({'message': 'invalid command', 'audio_b64': audio_b64})

def exec(cmd):
    if 'google search' in cmd:
        cmd = cmd.split('google search')
        term = cmd[1].strip()
        if 'about' in term.split(' ')[0]:
            term = term.replace('about', '')
        google_search(term)
        return respond(f'google searching {term}')

    if 'show my devices' in cmd:
        show_my_devices()
        return respond('showing your devices')

    if 'close window' in cmd:
        pyautogui.hotkey('alt', 'f4')
        return respond('closing')

    if 'maximize window' in cmd:
        pyautogui.press('f11')
        return respond('maximizing')
    
    if 'move window right' in cmd:
        pyautogui.hotkey('winleft', 'right')
        return respond('done')
    
    if 'move window left' in cmd:
        pyautogui.hotkey('winleft', 'left')
        return respond('done')

    if 'test' in cmd:
        return respond('TEST COMMAND')

    if 'generate speech' in cmd:
        cmd = cmd.split('generate speech')
        term = cmd[1].strip()
        return respond(term)

    if 'thanks' in cmd or 'thank you' in cmd:
        return respond("You're Welcome")

    else:
        return respond('invalid command')
