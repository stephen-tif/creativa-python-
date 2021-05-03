#       #############
#       ##         ##
#       #  ~~   ~~  # 
#       #  ()   ()  # 
#       (     ^     )
#        |         |
#        |  {===}  |
#         \       /
#        /  -----  \
#     ---  |%\ /%|  ---
#    /     |%%%%%|     \
#   /      |%/ \%|      \
#  ╔═════════════════════════╗ 
#  ║    MADE BY TIF MASTER   ║
#  ║    Date: 03/05/2021     ║
#  ╚═════════════════════════╝

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    param = {'category': "Better Call Saul"}
    response = requests.get(
        "https://breakingbadapi.com/api/characters", params=param).content
    jsonData = json.loads(response)
    return render_template('personajes.html', data=jsonData)


@app.route('/personaje/<id>')
def findPersonaje(id):
    param = {'category': "Better Call Saul"}
    response = requests.get(
        "https://breakingbadapi.com/api/characters/"+id, params=param).content
    jsonData = json.loads(response)
    return render_template('personaje-detail.html', data=jsonData)


@app.route('/personajeByName/<nombre>')
def findPersonajeByName(nombre):
    param = {'name': nombre}
    response = requests.get(
        "https://breakingbadapi.com/api/characters", params=param).content
    jsonData = json.loads(response)
    return render_template('personaje-detail.html', data=jsonData)


if __name__ == '__main__':
    app.run(debug=True)
