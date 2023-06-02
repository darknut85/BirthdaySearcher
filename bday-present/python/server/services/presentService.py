import config

class Get:

    def connectionString():
            conn = config.ConnectionString.returnConn()
            conn.autocommit = True
            return conn.cursor()

    def GetPresents():
        cs = Get.connectionString()
        cs.execute('''SELECT * from presents''')

        columns = cs.description
        results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cs.fetchall()]
        return results

    def GetPresentById(id):
        recordsToInsert = (id)

        cs = Get.connectionString
        cs.execute("SELECT * from presents WHERE id = %s", recordsToInsert)

        columns = cs.description
        results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cs.fetchall()]
        return results

    def AddPresent(recordToInsert):
        cs = Get.connectionString
        cs.execute("INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)", recordToInsert)
        cs.commit()

        present = { 'Id': '2', 'name': 'Flower', 'Owner': 'Isaac'}

        return present

    def DeletePresent(id):
        cs = Get.connectionString
        recordsToInsert = (id)
        cs.execute("DELETE from presents WHERE id = %s", recordsToInsert)
        cs.commit()

        return recordsToInsert

    def UpdatePresent(recordToInsert):
        cs = Get.connectionString
        cs.execute("UPDATE presents SET name = %s WHERE id = %s", recordToInsert)
        cs.commit()

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