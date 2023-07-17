import unittest
import os
import json
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(data)
        self.assertIsInstance(json_string, str)
        data_back = json.loads(json_string)
        self.assertEqual(data, data_back)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertIsInstance(data, list)
        json_string_back = Base.to_json_string(data)
        self.assertEqual(json_string, json_string_back)


if __name__ == '__main__':
    unittest.main()
