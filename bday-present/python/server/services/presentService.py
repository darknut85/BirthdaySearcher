import json
from objects.present import Present

p1 = Present('1', 'Lego', 'Holly')
p2 = Present('2' ,'Flowers' , 'Diego')
p3 = Present('3', 'Dragon', 'Sandy')

dd = json.dumps(p1)

presents = dd

def getPresents():
    return presents