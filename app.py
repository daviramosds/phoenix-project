from flask import Flask, request, send_file
from lib import commands

app = Flask(__name__)

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
    return send_file(f'audio/tmp/{file_id}.mp3')
