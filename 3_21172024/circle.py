

import unittest
import math

class Circle:

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius**2
    
    def get_circumference(self) -> float:
        return 2 * math.pi * self.radius


class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle(radius=3)

    def test_CalculateCircumference(self):
        circumference = self.circle.get_circumference()
        self.assertEqual(circumference, 2 * math.pi * 3)

    def test_CalculateArea(self):
        area = self.circle.get_area()
        self.assertAlmostEqual(area, math.pi * 3**2)

if __name__ == "__main__":
    unittest.main()
