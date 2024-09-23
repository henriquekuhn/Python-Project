from sqlalchemy import Column, Integer, String
import unittest
from main import DatabaseManagement

DB_NAME = 'test_db'
TABLE_NAME = 'TestTable'

class TestDatabaseManagement(unittest.TestCase):
    def setUp(self):
        # Criar uma instância do gerenciador de banco de dados
        self.db_manager = DatabaseManagement()
        # Conectar à engine do banco de dados com timeout
        self.assertEqual(self.db_manager.connect_engine(), 'Pass')
    
    def test_1_create_datbase(self):
        # Criar o banco de dados 'new_database' se ainda não existir
        self.assertEqual(self.db_manager.create_database(DB_NAME).upper(), DB_NAME.upper())

    def test_2_create_table(self):
        
        table_columns = {
            'id': 'INT AUTO_INCREMENT PRIMARY KEY',
            'name': 'VARCHAR(50)',
            'age': 'INT'
        }
        self.assertEqual(self.db_manager.create_table(DB_NAME, TABLE_NAME, table_columns).upper(), TABLE_NAME.upper())
#    
    def test_3_create_register(self):
        register = {
            'name': 'Rosbiff',
            'age': 30
        }
        result = self.db_manager.create_register(DB_NAME, TABLE_NAME, register)
        self.assertEqual(result, "Pass")
#
    def test_4_query_data(self):
        query = "Rosbiff"
        result = self.db_manager.query_data(DB_NAME, TABLE_NAME, value=query)
        self.assertEqual(result, "Pass")  
#    
    def test_5_query_table_with_filter(self):
        filters = {'id': 1}
        result = self.db_manager.query_data(DB_NAME, TABLE_NAME, filters=filters)
        self.assertEqual(result, "Pass")  
#
    def test_6_add_column(self):
        column_name = {'email': 'VARCHAR(50)'}
        result = self.db_manager.add_column(DB_NAME, TABLE_NAME, column_name)
        self.assertEqual(result, "Pass")  

#TODO: update_db
#    def test_7_update_db(self):

#TODO: delete_db
#    def test_8_delete_db(self):

#TODO: dell_column
#    def test_8_dell_column(self):


if __name__ == '__main__':
    # For Single tests:
    #suite = unittest.TestSuite()
    #suite.addTest(TestDatabaseManagement('test_1_create_datbase'))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()