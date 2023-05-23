import json
from config import ConnectionString
from objects.present import Present

def GetPresents():
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * from presents''')

    columns = cursor.description
    results = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    conn.commit()
    conn.close()
    return results

presents: Present = GetPresents()
#p3 = Present('3', 'Dragon', 'Sandy')

def getPresents():
    return presents