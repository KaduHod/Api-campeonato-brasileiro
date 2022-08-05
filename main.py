# Criar api REST que retorna a tabela do brasileirao com flesk
from flask import Flask, Response
from src.service import getTabelaBrasileirao
import json

app = Flask(__name__)

@app.route("/tabela-brasileirao/hoje")
def tabela():
    tabela = getTabelaBrasileirao.main()
    jsonData = json.dumps(tabela)
    return jsonData, 200, {'Content-Type': 'application/json;' }