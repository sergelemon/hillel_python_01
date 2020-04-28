import unittest

class TestBaseParser(unittest.TestCase):
    def setUp(self):
        test_url = 'test.com'
        parser = BaseParser(test_url)

    def test_work(self):
        # self.parser.work()
        pass

    def test_get_html(self):
        # self.parser.work()
        pass

    def test_save_data(self):
        # self.parser.work()
        pass


class TestNVParser(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()