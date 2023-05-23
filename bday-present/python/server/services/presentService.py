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

def GetPresentById():
    query = "SELECT * from presents WHERE id = %s"
    recordsToInsert = ('2')

    cursor.execute(query, recordsToInsert)

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    print(results)
    conn.commit()
    return results

def AddPresents():

    query = "INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)"
    recordsToInsert = (2, 'Flower', 'Isaac')
    cursor.execute(query, recordsToInsert)
    conn.commit()

def DeletePresents():

    recordsToInsert = ('2')
    query = "DELETE from presents WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()

def UpdatePresents():
    recordsToInsert = ('Car', '2')
    query = "UPDATE presents SET name = %s WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()



def getPresents():
    return GetPresents()

def getPresentById():
    return GetPresentById()

def addPresents():
    AddPresents()

def deletePresents():
    DeletePresents()

def updatePresents():
    UpdatePresents()