import psycopg2
import config

class Get:
    def GetPresents():
        with psycopg2.connect(database="birthdayPresent", user='postgres', password='Soraheliatos2@', host='127.0.0.1', port= '1700') as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * from presents')
                columns = cursor.description
                results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
                return results

    def GetPresentById(id):
        recordsToInsert = (id)

        cs = config.ConnectionString.returnConn()
        cs.execute("SELECT * from presents WHERE id = %s", recordsToInsert)

        columns = cs.description
        results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cs.fetchall()]
        return results

    def AddPresent(recordToInsert):
        cs = config.ConnectionString.returnConn()
        cs.execute("INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)", recordToInsert)

        present = { 'Id': '2', 'name': 'Flower', 'Owner': 'Isaac'}

        return present

    def DeletePresent(id):
        cs = config.ConnectionString.returnConn()
        recordsToInsert = (id)
        cs.execute("DELETE from presents WHERE id = %s", recordsToInsert)

        return recordsToInsert

    def UpdatePresent(recordToInsert):
        cs = config.ConnectionString.returnConn()
        cs.execute("UPDATE presents SET name = %s WHERE id = %s", recordToInsert)

        return recordToInsert



    def getPresents():
        return Get.GetPresents()

    def getPresentById(id):
        return Get.GetPresentById(id)

    def addPresent(recordToInsert):
        return Get.AddPresent(recordToInsert)

    def deletePresent(id):
        return Get.DeletePresent(id)

    def updatePresent(recordToInsert):
        return Get.UpdatePresent(recordToInsert)