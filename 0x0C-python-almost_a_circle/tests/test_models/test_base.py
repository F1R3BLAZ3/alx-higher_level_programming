import unittest
import os
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        # Ensure that the ID is assigned correctly
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        # Ensure that custom ID is assigned correctly
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        # Ensure that to_json_string returns a JSON string
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(data)
        self.assertIsInstance(json_string, str)

        # Ensure that the JSON string can be converted back to
        # a list of dictionaries
        data_back = json.loads(json_string)
        self.assertEqual(data, data_back)

    def test_from_json_string(self):
        # Ensure that from_json_string returns a list of dictionaries
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertIsInstance(data, list)

        # Ensure that the list of dictionaries can be converted back
        # to a JSON string
        json_string_back = Base.to_json_string(data)
        self.assertEqual(json_string, json_string_back)


if __name__ == '__main__':
    unittest.main()
