import unittest

from rectangle import area, perimeter


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


if __name__ == "__main__":
    unittest.main()
