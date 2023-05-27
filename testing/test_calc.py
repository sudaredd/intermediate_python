import unittest
from calc import add, sub, mul, div

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(23, 32), 55)
        self.assertEqual(add(-10, 10), 0)
        self.assertEqual(add(-7, -9), -16)

    def test_sub(self):
        self.assertEqual(sub(23, 32), -9)
        self.assertEqual(sub(-10, 10), -20)
        self.assertEqual(sub(-7, -9), 2)


    def test_mul(self):
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-10, 10), -100)
        self.assertEqual(mul(-7, -9), 63)


    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(5, 2), 2.5)
        self.assertRaises(ValueError, div, 5, 0)
        with self.assertRaises(ValueError):
            div(3, 0)



if __name__ == '__main__':
    unittest.main()