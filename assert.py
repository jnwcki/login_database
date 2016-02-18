"""
import unittest
from db_model import DBReader


class DBTest(unittest.TestCase):

    def test_db_reader_can_format_expected_file_structure(self):
        expected_input = ["jnowicki,pass,orange,steak and cheese", "user,pass,color,food"]
        expected_output = [["jnowicki", "pass", "orange", "steak and cheese"], ["user", "pass", "color", "food"]]
        db_reader = DBReader()
        self.assertEqual(db_reader.read_file(expected_input), expected_output)

    def test_db_reader_can_format_expected_file_structure_init(self):
        expected_input = ["jude nowicki,33,160", "bea,120,14"]
        expected_output = [["jude nowicki", "33", "160"], ["bea", "120", "14"]]
        db_reader = DBReader()
        self.assertEqual(db_reader.cleaned_data, expected_output)
"""



