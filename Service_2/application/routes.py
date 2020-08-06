from application import app
import random


@app.route('/race', methods=['GET'])
def race():

	list = ['Human','Super Mutant','Ghoul','Synth','Robot']
	
	return list[random.randrange(4)]