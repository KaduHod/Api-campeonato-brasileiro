from flask import Flask
from src.service import getTabelaBrasileirao, clubs
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    file = open('./index.html').read()
    return file, 200, {'Content-Type':'text/html; charset=utf-8'}

@app.route("/tabela-brasileirao/hoje", methods=['GET'])
def tabela():
    tabela = getTabelaBrasileirao.main()
    jsonData = json.dumps(tabela)
    return jsonData, 200, {'Content-Type': 'application/json;' }

@app.route("/cbf/clubs-ids", methods=["GET"])
def clubsIds():
    clubes = clubs.main()
    jsonData = json.dumps(clubes)
    return jsonData, 200, {'Content-Type': 'application/json;' }
