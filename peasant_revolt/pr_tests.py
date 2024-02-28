import unittest
import peasant_revolt

class PeasantRevoltTests(unittest.TestCase):
    def setUp(self):
        self.game = peasant_revolt.create_game()

    def test_initial_move(self):
        self.assertEqual(self.game['turn'], 'White')


if __name__=='__main__':
    unittest.main()
