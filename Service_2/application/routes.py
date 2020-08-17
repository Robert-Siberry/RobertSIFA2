from application import app
from flask import render_template, request
import requests
import random

@app.route('/race', methods=['GET'])
def race():
    list = ['Human','Synth','Robot','Super Mutant','Ghoul','Dog']
    return list[random.randrange(5)]
