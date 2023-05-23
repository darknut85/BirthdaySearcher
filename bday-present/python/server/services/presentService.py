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
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    cursor = conn.cursor()

    recordsToInsert = ('Car', '2')
    query = "UPDATE presents SET name = %s WHERE id = %s"
    cursor.execute(query, recordsToInsert)
    conn.commit()



def getPresents():
    return GetPresents()

def addPresents():
    AddPresents()

def deletePresents():
    DeletePresents()

def updatePresents():
    UpdatePresents()