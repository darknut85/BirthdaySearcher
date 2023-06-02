import services.presentService
from flask_cors import CORS
from main import start

app = start()
CORS(app)

@app.get('/presents')

@app.route('/presents/Get')
def Get():
    return services.presentService.Get.GetPresents()

@app.route('/presents/GetById')
def GetById():
    return services.presentService.Get.GetPresentById('2')

@app.route('/presents/Add')
def Add():
    recordsToInsert = ('2', 'Flower', 'Isaac')
    return services.presentService.Get.AddPresent(recordsToInsert)

@app.route('/presents/Delete')
def Delete():
    return services.presentService.Get.DeletePresent('2')

@app.route('/presents/Update')
def Update():
    recordToInsert = ('Car', '2')
    return services.presentService.Get.UpdatePresent(recordToInsert)