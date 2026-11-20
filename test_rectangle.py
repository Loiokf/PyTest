import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        res = area(3, 5)
        self.assertEqual(res, 15)

    def test_area_zero(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(3, 5)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
