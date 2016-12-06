import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('yuhao', 'chen')
        self.assertEqual(formatted_name, 'Yuhao Chen')

    def test_middle_name(self):
        formatted_name = get_formatted_name('yuhao', 'chen', 'howe')
        self.assertEqual(formatted_name, 'Yuhao Howe Chen')

unittest.main()
