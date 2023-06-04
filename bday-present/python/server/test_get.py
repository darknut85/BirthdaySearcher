import unittest
from unittest import mock
import psycopg2
import services.presentService as presentService

def ex():
    with psycopg2.connect("") as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * from presents')
            return cursor.fetchall()
        
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.present = [{'id':500,'name':'Dragon','owner':'Budew'}]
        self.dict = {"a":{'id':500, 'name':'Dragon','owner':'Budew'}}

    def tearDown(self):
        print('tearDown\n')

    @mock.patch('psycopg2.connect')
    def test_moqGet(self,mock_connect):
        mock_connect().__enter__().cursor().__enter__().fetchall.return_value = [self.present]
        value = presentService.Get.GetPresents()
        mock_connect().__enter__().cursor().__enter__().execute.assert_called_with('SELECT * from presents')
        
        a = value[0].values()
        b = self.dict.values()
        print("mock: ")
        print(a)
        print("expected: ")
        print(b)

        self.assertEqual(str(a), str(b))

if __name__ == '__main__':
    unittest.main()