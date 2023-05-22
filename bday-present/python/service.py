from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/sayHello')

@app.route('/sayHello/hi')
def Hi():
    return "Hi"