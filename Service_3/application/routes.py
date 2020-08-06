from application import app
import random


@app.route('/role', methods=['GET'])
def role():

	list = ['Hunter','Mechanic','Prospecter','Fighter','Medic','Trader','Leader']
	
	return list[random.randrange(6)]