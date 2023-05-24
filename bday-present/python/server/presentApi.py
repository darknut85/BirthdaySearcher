from flask_cors import CORS
from services.presentService import addPresent, getPresents, deletePresent, updatePresent, getPresentById
from main import start

app = start()
CORS(app)

@app.get('/presents')

@app.route('/presents/Get')
def Get():
    return getPresents()

@app.route('/presents/GetById')
def GetById():
    return getPresentById()

@app.route('/presents/Add')
def Add():
    return addPresent()

@app.route('/presents/Delete')
def Delete():
    return deletePresent()

@app.route('/presents/Update')
def Update():
    return updatePresent()

#getbyId
#delete
#update