import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_id_generation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        dict_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_string = Base.to_json_string(dict_list)
        expected_json = (
            '[{"id": 1, "name": "John"},'
            ' {"id": 2, "name": "Jane"}]'
        )
        self.assertEqual(json_string, expected_json)

        empty_list = []
        empty_json = Base.to_json_string(empty_list)
        self.assertEqual(empty_json, "[]")

    def test_from_json_string(self):
        json_string = (
            '[{"id": 1, "name": "John"},'
            ' {"id": 2, "name": "Jane"}]'
        )
        dict_list = Base.from_json_string(json_string)
        expected_list = [
            {'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Jane'}
        ]
        self.assertEqual(dict_list, expected_list)

        empty_json = "[]"
        empty_list = Base.from_json_string(empty_json)
        self.assertEqual(empty_list, [])

    def test_save_to_file(self):
        instances = [Base(1), Base(2)]
        Base.save_to_file(instances)

        with open("Base.json", "r") as file:
            json_data = file.read()
            expected_json = '[{"id": 1}, {"id": 2}]'
            self.assertEqual(json_data, expected_json)

    def test_create(self):
        attributes = {'id': 1, 'name': 'John'}
        instance = Base.create(**attributes)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'John')

    def test_load_from_file(self):
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)


if __name__ == '__main__':
    unittest.main()
