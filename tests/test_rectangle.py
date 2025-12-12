import unittest

from geometric_lib.rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        """Если одна из сторон равна 0, площадь должна быть 0."""
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)

    def test_area_normal(self):
        """Обычная площадь прямоугольника."""
        self.assertEqual(area(10, 5), 50)

    def test_area_commutativity(self):
        """Порядок сторон не должен влиять на площадь."""
        self.assertEqual(area(3, 7), area(7, 3))

    def test_perimeter_zero_side(self):
        """Периметр при стороне 0 (формула всё равно работает)."""
        self.assertEqual(perimeter(0, 5), (0 + 5) * 2)
        self.assertEqual(perimeter(10, 0), (10 + 0) * 2)

    def test_perimeter_normal(self):
        """Обычный периметр прямоугольника."""
        self.assertEqual(perimeter(4, 9), (4 + 9) * 2)

    def test_perimeter_commutativity(self):
        """Порядок сторон не должен влиять на периметр."""
        self.assertEqual(perimeter(3, 7), perimeter(7, 3))

    def test_area_negative_one_side(self):
        """Отрицательная одна сторона даёт отрицательную площадь по текущей реализации."""
        self.assertEqual(area(-3, 4), -12)

    def test_area_both_sides_negative(self):
        """Две отрицательные стороны дают положительную площадь."""
        self.assertEqual(area(-3, -4), 12)

    def test_perimeter_with_negative_side(self):
        """Периметр с отрицательной стороной считается формально по формуле."""
        self.assertEqual(perimeter(-3, 4), 2 * (-3 + 4))  # 2

    def test_area_invalid_type(self):
        """Строка вместо стороны должна приводить к TypeError."""
        with self.assertRaises(TypeError):
            area("a", 5)
        with self.assertRaises(TypeError):
            area(5, "b")

    def test_perimeter_invalid_type(self):
        """None вместо стороны должен приводить к TypeError."""
        with self.assertRaises(TypeError):
            perimeter(None, 5)
        with self.assertRaises(TypeError):
            perimeter(5, None)


if __name__ == "__main__":
    unittest.main()
