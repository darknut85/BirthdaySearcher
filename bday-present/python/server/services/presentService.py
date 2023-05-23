from config import ConnectionString

def AddPresents():
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    cursor = conn.cursor()
    query = "INSERT INTO presents(ID, NAME, OWNER) VALUES(%s, %s, %s)"
    recordsToInsert = (2, 'Flower', 'Isaac')
    cursor.execute(query, recordsToInsert)
    conn.commit()

def GetPresents():
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * from presents''')

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    conn.commit()
    return results

def getPresents():
    return GetPresents()

def addPresents():
    AddPresents()