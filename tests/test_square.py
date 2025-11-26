import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        """Площадь квадрата со стороной 0 должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_positive_side(self):
        """Площадь квадрата со стороной > 0."""
        self.assertEqual(area(5), 25)

    def test_area_float_side(self):
        """Площадь квадрата с дробной стороной."""
        self.assertAlmostEqual(area(2.5), 6.25, places=7)

    def test_perimeter_zero_side(self):
        """Периметр квадрата со стороной 0 должен быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_side(self):
        """Периметр квадрата со стороной > 0."""
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_float_side(self):
        """Периметр квадрата с дробной стороной."""
        self.assertAlmostEqual(perimeter(2.5), 10.0, places=7)


if __name__ == "__main__":
    unittest.main()
