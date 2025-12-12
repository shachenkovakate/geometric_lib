import unittest

from geometric_lib.triangle import area, perimeter


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

    def test_area_negative_base_or_height(self):
        """Отрицательное основание или высота: формула даёт отрицательную площадь."""
        self.assertEqual(area(-3, 4), -3 * 4 / 2)
        self.assertEqual(area(3, -4), 3 * -4 / 2)

    def test_perimeter_negative_side(self):
        """Отрицательная сторона: периметр считается формально по формуле."""
        self.assertEqual(perimeter(-3, 4, 5), -3 + 4 + 5)

    def test_perimeter_degenerate_triangle(self):
        """'Невозможный' треугольник: функция всё равно просто суммирует стороны."""
        self.assertEqual(perimeter(1, 2, 10), 13)

    def test_area_invalid_type(self):
        """Строка вместо основания или высоты должна приводить к TypeError."""
        with self.assertRaises(TypeError):
            area("base", 4)
        with self.assertRaises(TypeError):
            area(3, "height")

    def test_perimeter_invalid_type(self):
        """None или строка вместо стороны должны приводить к TypeError."""
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "b", 5)


if __name__ == "__main__":
    unittest.main()
