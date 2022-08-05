# Criar api REST que retorna a tabela do brasileirao com flesk
from flask import Flask, Response
from src.service import tabelaBrasileirao
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/tabela-brasileirao")
def tabela():
    tabela = tabelaBrasileirao.main()
    jsonData = json.dumps(tabela)
    
    
    return jsonData, 200, {'Content-Type': 'application/json;' }