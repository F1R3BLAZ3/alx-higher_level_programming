import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_attributes(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s.size = 7
        self.assertEqual(s.area(), 49)

    def test_display(self):
        s = Square(3)
        captured_output = []
        try:
            import sys
            from io import StringIO

            sys.stdout = StringIO()
            s.display()
            captured_output.append(sys.stdout.getvalue().strip())
        finally:
            sys.stdout = sys.__stdout__

        expected_output = "###\n###\n###"
        self.assertEqual(captured_output[0], expected_output)

    def test_to_string(self):
        s = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(s.id, 10)

        s.update(10, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)

        s.update(10, 7, 15)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 15)

        s.update(10, 7, 15, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 15)
        self.assertEqual(s.y, 4)

        s.update(x=12)
        self.assertEqual(s.x, 12)

        s.update(y=6)
        self.assertEqual(s.y, 6)

        s.update(size=3)
        self.assertEqual(s.size, 3)

    def test_dictionary_representation(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)

    # Additional tests
    def test_invalid_size_value(self):
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            s = Square(5, -2, 3)

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            s = Square(5, 2, -3)

    def test_to_dictionary_with_invalid_input(self):
        s = Square(5, 2, 3, 1)
        invalid_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3,
                        'invalid_attribute': 42}
        valid_dict = s.to_dictionary()
        self.assertDictEqual(valid_dict, {'id': 1, 'size': 5, 'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
