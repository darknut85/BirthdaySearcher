from config import ConnectionString
from objects.presents import Presents

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

def GetPresentById():
    query = "SELECT * from presents WHERE id = %s"
    recordsToInsert = ('2')

    cursor.execute(query, recordsToInsert)

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    print(results)
    conn.commit()
    return results

def AddPresent():

    query = "INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)"
    recordsToInsert = ('2', 'Flower', 'Isaac')
    cursor.execute(query, recordsToInsert)
    conn.commit()

    present = { 'Id': '2', 'name': 'Flower', 'Owner': 'Isaac'}

    return present

def DeletePresent():

    recordsToInsert = ('2')
    query = "DELETE from presents WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()

    return recordsToInsert

def UpdatePresent():
    recordsToInsert = ('Car', '2')
    query = "UPDATE presents SET name = %s WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()

    return recordsToInsert



def getPresents():
    return GetPresents()

def getPresentById():
    return GetPresentById()

def addPresent():
    return AddPresent()

def deletePresent():
    return DeletePresent()

def updatePresent():
    return UpdatePresent()