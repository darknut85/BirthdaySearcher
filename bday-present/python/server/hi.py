from flask import Flask, request
from flask_cors import CORS

first = 0
second = 0
answer = 0

app = Flask(__name__)
CORS(app)

@app.get('/sayHello')

@app.route('/sayHello/Hi')
def Hi():
    return "Hi"