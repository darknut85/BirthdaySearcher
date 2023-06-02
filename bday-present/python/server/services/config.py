import psycopg2

conn = psycopg2.connect(
   database="birthdayPresent", user='postgres', password='Soraheliatos2@', host='127.0.0.1', port= '1700'
)
class ConnectionString():
    def returnConn():
        return conn