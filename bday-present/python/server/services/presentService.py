from config import ConnectionString

def connectionString():
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    return conn

def GetPresents():

    cs = connectionString.cursor()
    cs.execute('''SELECT * from presents''')

    columns = cs.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    return results

def GetPresentById(id):
    recordsToInsert = (id)

    cs = connectionString.cursor()
    cs.execute("SELECT * from presents WHERE id = %s", recordsToInsert)

    columns = cs.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    return results

def AddPresent(recordToInsert):
    cs = connectionString.cursor()
    cs.execute("INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)", recordToInsert)
    cs.commit()

    present = { 'Id': '2', 'name': 'Flower', 'Owner': 'Isaac'}

    return present

def DeletePresent(id):
    cs = connectionString.cursor()
    recordsToInsert = (id)
    cs.execute("DELETE from presents WHERE id = %s", recordsToInsert)
    cs.commit()

    return recordsToInsert

def UpdatePresent(recordToInsert):
    cs = connectionString.cursor()
    cs.execute("UPDATE presents SET name = %s WHERE id = %s", recordToInsert)
    cs.commit()

    return recordToInsert



def getPresents():
    return GetPresents()

def getPresentById(id):
    return GetPresentById(id)

def addPresent(recordToInsert):
    return AddPresent(recordToInsert)

def deletePresent(id):
    return DeletePresent(id)

def updatePresent(recordToInsert):
    return UpdatePresent(recordToInsert)