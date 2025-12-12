import math
import unittest

from geometric_lib.circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        """Площадь круга с r = 0 должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_positive_radius(self):
        """Площадь круга с положительным радиусом."""
        r = 2
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_area_float_radius(self):
        """Площадь круга с дробным радиусом."""
        r = 1.5
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_perimeter_zero_radius(self):
        """Длина окружности при r = 0 должна быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_radius(self):
        """Длина окружности с положительным радиусом."""
        r = 3
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected, places=7)

    def test_perimeter_float_radius(self):
        """Длина окружности с дробным радиусом."""
        r = 2.5
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected, places=7)

    def test_area_negative_radius(self):
        """При отрицательном радиусе формула всё равно даёт положительную площадь."""
        r = -3
        expected = math.pi * r * r  # r*r > 0
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_perimeter_negative_radius(self):
        """При отрицательном радиусе длина окружности получается отрицательной."""
        r = -3
        expected = 2 * math.pi * r  # < 0
        self.assertAlmostEqual(perimeter(r), expected, places=7)

    def test_area_invalid_type(self):
        """Строка вместо радиуса должна приводить к TypeError."""
        with self.assertRaises(TypeError):
            area("not a radius")

    def test_perimeter_invalid_type(self):
        """None вместо радиуса должен приводить к TypeError."""
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == "__main__":
    unittest.main()
