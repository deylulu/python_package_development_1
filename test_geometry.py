# %%
import unittest
from geometry import Point, Line

class TestGeometry(unittest.TestCase):

    def test_point(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance_to(p2), 5.0)

    def test_line(self):
        p1 = Point(0, 0)
        p2 = Point(6, 8)
        line = Line(p1, p2)
        self.assertEqual(line.length(), 10.0)

if __name__ == "__main__":
    unittest.main()


