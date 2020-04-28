import unittest
from sea_fight import Game

class Test_Game(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_make_table(self):
        table = self.game._make_table()
        self.assertTrue(table)
        self.assertIsInstance(table, list)

if __name__ == '__main__':
    unittest.main()