import services.presentService as presentService
from flask_cors import CORS
from main import start

app = start()
CORS(app)

@app.get('/presents')

@app.route('/presents/Get')
def Get():
    return presentService.Get.GetPresents()

@app.route('/presents/GetById')
def GetById():
    return presentService.Get.GetPresentById('2')

@app.route('/presents/Add')
def Add():
    recordsToInsert = ('2', 'Flower', 'Isaac')
    return presentService.Get.AddPresent(recordsToInsert)

@app.route('/presents/Delete')
def Delete():
    return presentService.Get.DeletePresent('2')

@app.route('/presents/Update')
def Update():
    recordToInsert = ('Car', '2')
    return presentService.Get.UpdatePresent(recordToInsert)