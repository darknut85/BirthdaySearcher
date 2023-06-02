import unittest
from unittest.mock import patch
import presentService

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.present = {'id':2,'name':'Flower','owner':'Isaac'}

    def tearDown(self):
        print('tearDown\n')

    def test_get(self):
        results = presentService.GetPresents()
        self.assertTrue(results[0] == self.present)

#cursor.execute('''SELECT * from presents''')
    #def test_moqGet(self):
        #with patch('cursor.execute("SELECT * from presents")') as mocked_get:
            #mocked_get.return_value.ok = self.present
            
            #results = presentService.GetPresents()
            #self.assertTrue(results[0] == self.present)


if __name__ == '__main__':
    unittest.main()