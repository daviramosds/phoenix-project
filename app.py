from flask import Flask, request, send_file
from os import getenv
from lib import commands, start
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

start.load_env()
start.handle_tmp_files()

@app.route("/cmd", methods=["POST"]) # BASE_URL/cmd/
def exec_cmd():
    data = request.json
    cmd = data.get('cmd')
    result = commands.exec(cmd)
    return result

@app.route('/audio') # BASE_URL/audio?id={id}
def get_audio_file():
    file_id = request.args.get('id')
    FILE_PATH = getenv('TMP_FILE_PATH')
    FILE_PREFIX = getenv('AUDIO_FILE_PREFIX')
    return send_file(f'{FILE_PATH}{FILE_PREFIX}{file_id}.mp3')