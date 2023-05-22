from flask_cors import CORS
from services.presentService import getPresents
from main import start

app = start()
CORS(app)

@app.get('/presents')

@app.route('/presents/Get')
def Hi():
    return getPresents()

#getbyId
#delete
#update