from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import random

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)

class fopnp(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    races = db.Column(db.String(50), nullable=False)
    roles = db.Column(db.String(50), nullable=False)
   
    def __repr__(self):
        return ''.join(
        [
            'Race: ' + self.races + '\n' 
            'Roles ' + self.roles + '\n'
            'ID: ' + str(self.id) 
        ]
    )

@app.route('/merge', methods=['GET', 'POST'])
def merge():
    race = requests.get('http://service_2:5001/race').text
    role = requests.get('http://service_3:5002/role').text
    response = "Your character is a " + str(race) + " " + str(role)
    fopnp_data = fopnp(
            races=str(race),
            roles=str(role)
        )
    db.session.add(fopnp_data)
    db.session.commit()
    return response
