from flask import Flask, request, send_file
from os import getenv
from lib import commands, start

app = Flask(__name__)

start.remove_tmp_files() # removing old audio files
start.load_env()

@app.route("/cmd", methods=["POST"])
def exec_cmd():
    data = request.json
    cmd = data.get('cmd')
    result = commands.exec(cmd)
    return result

@app.route('/audio') # BASE_URL/audio?id={id}
def get_audio_file():
    file_id = request.args.get('id')
    print(file_id)
    AUDIO_FILE_PATH = getenv('AUDIO_FILE_PATH')
    return send_file(f'{AUDIO_FILE_PATH}{file_id}.mp3')
