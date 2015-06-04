import unittest
from outcome import Outcome 
from bin import Bin

o1 = Outcome('1',35)
o2 = Outcome('2',35)
o3 = Outcome('3',35)
o4 = Outcome('split bet', 17)

class bintest(unittest.TestCase):
    
    def test_outcomes(self):
        self.assertEqual(Bin(o1,o2,o3).outcomes,frozenset([o1,o2,o3]))
        self.assertNotEqual(Bin(o1).outcomes,frozenset([o1,o2,o3]))
        self.assertEqual(Bin(o1,o3).outcomes,frozenset([o1,o3]))
    
    def test_add(self):
        b1 = Bin()
        b1.add(o1)
        self.assertTrue(b1.outcomes == frozenset([o1]))

if __name__ == '__main__':
    unittest.main()
