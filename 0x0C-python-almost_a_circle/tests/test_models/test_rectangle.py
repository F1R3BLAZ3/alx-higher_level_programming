import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_attributes(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

        r.width = 7
        r.height = 6
        self.assertEqual(r.area(), 42)

    def test_display(self):
        r = Rectangle(3, 2)
        captured_output = []
        try:
            import sys
            from io import StringIO

            sys.stdout = StringIO()
            r.display()
            captured_output.append(sys.stdout.getvalue().strip())
        finally:
            sys.stdout = sys.__stdout__

        expected_output = "###\n###"
        self.assertEqual(captured_output[0], expected_output)

    def test_to_string(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(10)
        self.assertEqual(r.id, 10)

        r.update(10, 7)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)

        r.update(10, 7, 15)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)

        r.update(10, 7, 15, 4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 4)

        r.update(10, 7, 15, 4, 9)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 9)

        r.update(x=12)
        self.assertEqual(r.x, 12)

        r.update(y=6, width=3)
        self.assertEqual(r.y, 6)
        self.assertEqual(r.width, 3)

    def test_dictionary_representation(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
