import unittest
from database.mysql_connector import MySQLHandler

class TestMySQL(unittest.TestCase):
    def test_query_execution(self):
        db = MySQLHandler()
        result = db.query("SELECT * FROM users")
        self.assertGreater(len(result), 0)
