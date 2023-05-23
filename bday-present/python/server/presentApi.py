from flask_cors import CORS
from services.presentService import addPresents, getPresents
from main import start

app = start()
CORS(app)

@app.get('/presents')

@app.route('/presents/Get')
def Get():
    return getPresents()

@app.route('/presents/Add')
def Add():
    addPresents()

#getbyId
#delete
#update