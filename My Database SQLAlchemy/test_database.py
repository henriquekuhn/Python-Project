import unittest
from main import DatabaseManagement

class TestDatabaseManagement(unittest.TestCase):

    def setUp(self):
        self.db_management = DatabaseManagement()
        self.db_management.create_db()
        self.db_management.initiate_db_session()

    def test_2_create_test(self):
        result = self.db_management.create_test("Rosbiff", 25.0, 3.3, 0.8, 3.3, 10.7)
        self.assertEqual(result, "Test create success.")

    def test_3_query_db(self):
        self.size_1_test = self.db_management.query_test()
        self.db_management.create_test("Rosbiff", 25.0, 3.3, 0.8, 3.3, 3.3)
        self.size_2_test = self.db_management.query_test()
        self.assertEqual(self.size_2_test, self.size_1_test+1)  

    def test_4_queryfilter_db(self):
        column_search = "operator"
        search_name = "Rosbiff"
        self.result = self.db_management.query_by_filter(column_search, search_name)
        self.assertEqual(self.result, search_name)

    def test_5_update_db(self):
        search_name = "Rosbiff"
        new_value = "Chuck Norris"
        column_search = "operator"
        self.result = self.db_management.edit_register(column_search, search_name, new_value)
        self.assertEqual(self.result, new_value)

    def test_6_delete_db(self):
        self.search_name = "Rosbiff"
        self.column_search = "operator"
        self.result = self.db_management.delete_register(self.column_search, self.search_name)
        print(self.result)
        self.assertEqual(self.result, None)

    def test_7_add_column(self):
        self.db_management.add_new_column('new_column', 'TEXT') #INTEGER, TEXT, FLOAT

    def test_8_dell_column(self):
        self.db_management.delete_column('new_column')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDatabaseManagement('test_2_create_test'))
    #suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestDatabaseManagement))

    runner = unittest.TextTestRunner()
    runner.run(suite)