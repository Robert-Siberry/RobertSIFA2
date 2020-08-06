from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    character = requests.get('http://localhost:5003/character')
    print(character)
    character = character.text
    return render_template('index.html', character = character, title = 'Home')
