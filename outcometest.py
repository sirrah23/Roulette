import unittest
from outcome import Outcome

o1 = Outcome("1",35)
o2 = Outcome("1",35)
o3 = Outcome("split bet",17)

class OutcomeTests(unittest.TestCase):
    
    def test_equality_same(self):
        self.assertEqual(o1,o2)

    def test_equality_diff(self):
        self.assertNotEqual(o1,o3)
        self.assertNotEqual(o2,o3)
    
    def test_win_amount(self):
        self.assertEqual(o1.winAmount(1),35)
        self.assertEqual(o1.winAmount(2),70)
        self.assertEqual(o1.winAmount(3),105)

if __name__ == '__main__':
    unittest.main()
