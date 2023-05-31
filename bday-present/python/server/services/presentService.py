from config import ConnectionString

conn = ConnectionString.returnConn()
conn.autocommit = True
cursor = conn.cursor()

def GetPresents():

    query = '''SELECT * from presents'''
    cursor.execute(query)

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    conn.commit()
    return results

def GetPresentById(id):
    query = "SELECT * from presents WHERE id = %s"
    recordsToInsert = (id)

    cursor.execute(query, recordsToInsert)

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    print(results)
    conn.commit()
    return results

def AddPresent(recordToInsert):

    query = "INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)"
    cursor.execute(query, recordToInsert)
    conn.commit()

    present = { 'Id': '2', 'name': 'Flower', 'Owner': 'Isaac'}

    return present

def DeletePresent(id):

    recordsToInsert = (id)
    query = "DELETE from presents WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()

    return recordsToInsert

def UpdatePresent(recordToInsert):
    query = "UPDATE presents SET name = %s WHERE id = %s"
    cursor.execute(query, recordToInsert)
    conn.commit()

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