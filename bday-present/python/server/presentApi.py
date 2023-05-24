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
    return getPresentById('2')

@app.route('/presents/Add')
def Add():
    recordsToInsert = ('2', 'Flower', 'Isaac')
    return addPresent(recordsToInsert)

@app.route('/presents/Delete')
def Delete():
    return deletePresent('2')

@app.route('/presents/Update')
def Update():
    recordToInsert = ('Car', '2')
    return updatePresent(recordToInsert)

#getbyId
#delete
#update