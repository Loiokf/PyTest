import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_zero_height(self):
        res = area(6, 0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
