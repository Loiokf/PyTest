import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
