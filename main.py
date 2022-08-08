from flask import Flask
from src.service import getTabelaBrasileirao, clubs
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    file = open('./index.html').read()
    return file, 200, {'Content-Type':'text/html; charset=utf-8'}

@app.route("/uol/tabela-brasileirao/hoje", methods=['GET'])
def tabela():
    file = open('./src/service/tabela.json').read()
    jsonData = json.loads(file)
    return jsonData, 200, {'Content-Type': 'application/json;' }

@app.route('/wiki/tabela-brasileirao/hoje', methods=['GET'])
def wikiTable():
    file = open('./src/service/tabela-wiki.json').read()
    jsonData = json.loads(file)
    return jsonData, 200, {'Content-Type': 'application/json;' }

@app.route("/cbf/clubs", methods=["GET"])
def clubs():
    file = open('./src/service/clubs.json').read()
    jsonData = json.loads(file)
    return jsonData, 200, {'Content-Type': 'application/json;' }

@app.route("/cbf/athletes", methods=["GET"])
def athletes():
    file = open('./src/service/athletes.json').read()
    jsonData = json.loads(file)
    return jsonData, 200, {'Content-Type': 'application/json;' }