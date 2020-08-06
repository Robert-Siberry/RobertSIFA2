from application import app
import requests


@app.route('/character', methods=['GET'])
def character():
    race = requests.get('http://localhost:5001/race')
    role = requests.get('http://localhost:5002/role')
    character = race.text + " " + role.text
    return character