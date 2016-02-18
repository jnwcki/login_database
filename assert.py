import unittest
from db_model import DBReader
from main import Main

class DBTest(unittest.TestCase):

    def test_db_reader_can_format_expected_file_structure(self):
        expected_input = ["jnowicki,pass,orange,steak and cheese", "user,pass,color,food"]
        expected_output = [["jnowicki", "pass", "orange", "steak and cheese"], ["user", "pass", "color", "food"]]
        db_reader = DBReader()
        self.assertEqual(db_reader.clean_file(expected_input), expected_output)

    def test_db_reader_can_format_expected_file_structure_init(self):
        expected_input = ["jude nowicki,33,160", "bea,120,14"]
        expected_output = [["jude nowicki", "33", "160"], ["bea", "120", "14"]]
        db_reader = DBReader(expected_input)
        self.assertEqual(db_reader.cleaned_data, expected_output)

    def test_check_to_see_if_class_main_accepts_user_name(self):
        expected_input = "username"
        expected_output = "username"
        main_class = Main(expected_input)
        self.assertEqual(main_class.username, expected_output)

    def test_check_if_main_gets_username_from_db(self):
        expected_input = "username"
        expected_output = "username"
        main_class = Main(expected_input)
        self.assertEqual(main_class.get_username_from_db(expected_input), expected_output)


