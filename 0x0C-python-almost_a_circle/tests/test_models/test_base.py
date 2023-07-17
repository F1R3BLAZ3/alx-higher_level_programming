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

    def test_id_assignment_with_multiple_instances(self):
        # Create 100 instances and check their IDs
        instances = [Base() for _ in range(100)]
        self.assertEqual([instance.id for instance in instances], list(range(1, 101)))

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

    def test_from_json_string_with_invalid_input(self):
        # Test with valid JSON string but empty list
        empty_json_string = '[]'
        data = Base.from_json_string(empty_json_string)
        self.assertEqual(data, [])

        # Test with empty JSON string
        invalid_json_string = ''
        data = Base.from_json_string(invalid_json_string)
        self.assertEqual(data, [])

    def test_save_to_file_with_different_class_instances(self):
        # Create instances of derived classes (if available)
        # Assuming Rectangle and Square are derived from Base
        class Rectangle(Base):
            def __init__(self, width, height):
                super().__init__()
                self.width = width
                self.height = height

            def to_dictionary(self):
                return {'width': self.width, 'height': self.height}

        class Square(Base):
            def __init__(self, side):
                super().__init__()
                self.side = side

            def to_dictionary(self):
                return {'side': self.side}

        rectangles = [Rectangle(10, 5), Rectangle(7, 3)]
        squares = [Square(6), Square(4)]

        # Save instances to separate files
        Rectangle.save_to_file(rectangles)
        Square.save_to_file(squares)

        # Verify the files were created
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertTrue(os.path.exists("Square.json"))

        # Clean up: remove the created files
        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_load_from_file_with_invalid_json_files(self):
        # Test with non-existent file
        non_existent_file_instances = Base.load_from_file()
        self.assertEqual(non_existent_file_instances, [])

        # Test with empty file
        empty_file = "empty_file.json"
        with open(empty_file, 'w') as f:
            f.write("")
        empty_file_instances = Base.load_from_file()
        self.assertEqual(empty_file_instances, [])
        os.remove(empty_file)

    def test_create_method_with_invalid_inputs(self):
        # Test with an invalid dictionary for Rectangle
        with self.assertRaises(ValueError):
            invalid_rectangle_dict = {'invalid_attribute': 10, 'height': 5}
            Base.create(**invalid_rectangle_dict)

        # Test with an invalid dictionary for Square
        with self.assertRaises(ValueError):
            invalid_square_dict = {'side': 6, 'invalid_attribute': 42}
            Base.create(**invalid_square_dict)


if __name__ == '__main__':
    unittest.main()
