from app import get_distance
import unittest

class DistanceTest(unittest.TestCase):

    def test_long(self):
        l1 = "Voorhees, New Brunswick, NJ"
        l2 = "Metzger, Piscataway, NJ"
        dist =get_distance(l1, l2)
        self.assertEqual(dist, 11.7)
    
    def test_same_place(self):
        l1 = "Metzger, Piscataway, NJ"
        dist = get_distance(l1, l1)
        self.assertEqual(dist, 0)

    def test_invalid_address(self):
        l1 = "dawuhdhawdadhaud789132y91y23ipuhdwdjlknawkldbqwe1hepe"
        l2 = "Barr Hall, Piscataway, NJ"
        dist = get_distance(l1, l2)
        self.assertEqual(dist, None)

    def test_normal_1(self):
        l1 = "The Yard, New Brunswick, NJ"
        l2 = "Campbell, New Brunswick, NJ"
        dist = get_distance(l1, l2)
        self.assertAlmostEqual(dist, 2.5666666666666)
    
    def test_normal_2(self):
        l1 = "Voorhees, New Brunswick, NJ"
        l2 = "Scott Hall, New Brunswick, NJ"
        dist = get_distance(l1, l2)
        self.assertAlmostEqual(dist, 8.7)

    def test_normal_3(self):
        l1 = "Silvers Apartments, Piscataway, NJ"
        l2 = "Yhomas Suites, :iscataway, NJ"
        dist = get_distance(l1, l2)
        self.assertAlmostEqual(dist, 3.75)

    def test_normal_4(self):
        l1 = "Carnegie Mellon University, Pittsburgh, PA"
        l2 = "Silvers Apartments, Piscataway, NJ"
        dist = get_distance(l1, l2)
        self.assertAlmostEqual(dist, 329.4166666666667)

if __name__ == '__main__':
    unittest.main()