from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

presents = ['lego', 'flowers', 'dragon']

@app.get('/presents')

@app.route('/presents/Get')
def Hi():
    return presents

#getbyId
#delete
#update