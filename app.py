from flask import Flask, request
from lib import commands

app = Flask(__name__)

@app.route("/cmd", methods=["POST"])
def exec_cmd():
    data = request.json
    cmd = data.get('cmd')
    result = commands.exec(cmd)
    return result