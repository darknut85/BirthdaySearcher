import unittest
import psycopg2
from unittest.mock import patch
import services.presentService

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.present = {'id':2,'name':'Flower','owner':'Isaac'}

    def tearDown(self):
        print('tearDown\n')

    def test_get(self):
        results = services.presentService.Get.GetPresents()
        self.assertTrue(self.present == results[0])

#cursor.execute('''SELECT * from presents''')
    def test_moqGet(self):
        conn = psycopg2.connect(
        database="birthdayPresent", user='postgres', password='Soraheliatos2@', host='127.0.0.1', port= '1700')
        conn.autocommit = True

        with patch('config.ConnectionString.returnConn') as mocked_get:
            mocked_get.return_value = conn.cursor()

if __name__ == '__main__':
    unittest.main()