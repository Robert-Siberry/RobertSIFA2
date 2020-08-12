from application import app
from flask import render_template, request
import requests
import random

@app.route('/role', methods=['GET'])
def role():
    list = ['Prospector','Leader','Gunslinger','Mechanic','Figter','Trader']
    return list[random.randrange(5)]
