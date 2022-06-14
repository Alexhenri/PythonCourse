import unittest
from main import unzip_origin_file
from main import find_phone_re

class MyUnzipTest(unittest.TestCase):
    def test_unzip_name(self):
        name, dir = unzip_origin_file('teste')

        self.assertEqual(name, 'teste')  # add assertion here
        self.assertEqual(dir, '')  # add assertion here

class MyFindPhoneRe(unittest.TestCase):
    def test_find_phone(self):
        result = find_phone_re('dasdadasdsadad')
        if result:
            result = True
        else:
            result = False
        self.assertEqual(result, False)  # add assertion here

        result2 = find_phone_re('dasd123-124-555adasdsadad')
        if result2:
            result2 = True
        else:
            result2 = False
        self.assertEqual(result2, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
