from flask import Flask
from flask_cors import CORS
from services.presentService import getPresents

app = Flask(__name__)
CORS(app)

presents = getPresents()

@app.get('/presents')

@app.route('/presents/Get')
def Hi():
    return presents

#getbyId
#delete
#update