import json
from config import ConnectionString
from objects.present import Present

def GetPresents():
    conn = ConnectionString.returnConn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * from presents''')

    result = cursor.fetchall()
    print(result)

    conn.commit()
    conn.close()
    return result

presents = GetPresents()

def getPresents():
    return presents