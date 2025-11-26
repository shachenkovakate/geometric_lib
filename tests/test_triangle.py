import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base(self):
        """Если основание = 0, площадь должна быть 0."""
        self.assertEqual(area(0, 10), 0)

    def test_area_zero_height(self):
        """Если высота = 0, площадь должна быть 0."""
        self.assertEqual(area(10, 0), 0)

    def test_area_normal(self):
        """Обычная площадь треугольника."""
        self.assertEqual(area(10, 4), 10 * 4 / 2)

    def test_area_float(self):
        """Площадь треугольника с дробными параметрами."""
        self.assertAlmostEqual(area(2.5, 3.5), 2.5 * 3.5 / 2, places=7)

    def test_perimeter_normal(self):
        """Периметр треугольника с целыми сторонами."""
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        """Периметр треугольника с дробными сторонами."""
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 2.5 + 3.5 + 4.5, places=7)


if __name__ == "__main__":
    unittest.main()
