################################################################################
# UNIT TESTS
################################################################################

from interval import Interval
import numpy as np

import unittest


class test_interval_integers(unittest.TestCase):

    def runTest(self):

        interval = Interval(0, 100)

        with self.assertRaises(ValueError):
            interval[101]
        with self.assertRaises(ValueError):
            interval[-1]

        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,100.]: None}")
        self.assertEqual(interval[(0, 100)], [None])
        interval[(11, 30)] = "a"
        interval[(31, 60)] = "b"
        interval[(61, 90)] = "c"
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,11.): None, [11.,30.]: 'a', " +
                         "(30.,31.): None, [31.,60.]: 'b', " +
                         "(60.,61.): None, [61.,90.]: 'c', " +
                         "(90.,100.]: None}")

        self.assertEqual(interval[(0, 100)], [None, "a", "b", "c"])
        for i in range(0, 101):
            if i < 11:
                self.assertEqual(interval[i], None)
            elif i > 10 and i < 31:
                self.assertEqual(interval[i], "a")
            elif i > 30 and i < 61:
                self.assertEqual(interval[i], "b")
            elif i > 60 and i < 91:
                self.assertEqual(interval[i], "c")
            else:
                self.assertEqual(interval[i], None)

        interval[(15, 45)] = "d"
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,11.): None, [11.,15.): 'a', " +
                         "[15.,45.]: 'd', (45.,60.]: 'b', " +
                         "(60.,61.): None, [61.,90.]: 'c', " +
                         "(90.,100.]: None}")

        self.assertEqual(interval[(0, 100)], [None, "a", "b", "c", "d"])
        self.assertEqual(interval[(10, 40)], [None, "a", "d"])
        for i in range(0, 101):
            if i < 11:
                self.assertEqual(interval[i], None)
            elif i > 10 and i < 15:
                self.assertEqual(interval[i], "a")
            elif i > 14 and i < 46:
                self.assertEqual(interval[i], "d")
            elif i > 45 and i < 61:
                self.assertEqual(interval[i], "b")
            elif i > 60 and i < 91:
                self.assertEqual(interval[i], "c")
            else:
                self.assertEqual(interval[i], None)

        interval[(45, 100)] = "e"
        self.assertEqual(interval[(0, 100)], [None, "a", "d", "e"])
        for i in range(0, 101):
            if i < 11:
                self.assertEqual(interval[i], None)
            elif i > 10 and i < 15:
                self.assertEqual(interval[i], "a")
            elif i > 14 and i < 45:
                self.assertEqual(interval[i], "d")
            elif i > 44 and i < 101:
                self.assertEqual(interval[i], "e")

        interval[(50, 60)] = "c"
        self.assertEqual(interval[(0, 100)], [None, "a", "d", "e", "c"])
        for i in range(0, 101):
            if i < 11:
                self.assertEqual(interval[i], None)
            elif i > 10 and i < 15:
                self.assertEqual(interval[i], "a")
            elif i > 14 and i < 45:
                self.assertEqual(interval[i], "d")
            elif i > 44 and i < 50:
                self.assertEqual(interval[i], "e")
            elif i > 50 and i < 61:
                self.assertEqual(interval[i], "c")
            elif i > 60 and i < 101:
                self.assertEqual(interval[i], "e")

        interval[(-20, 20)] = "f"
        self.assertEqual(interval[(0, 100)], ["d", "e", "c", "f"])
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,20.]: 'f', (20.,45.): 'd', " +
                         "[45.,50.): 'e', [50.,60.]: 'c', (60.,100.]: 'e'}")

        interval[(90, 110)] = "g"
        self.assertEqual(interval[(0, 100)], ["d", "e", "c", "f", "g"])
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,20.]: 'f', (20.,45.): 'd', " +
                         "[45.,50.): 'e', [50.,60.]: 'c', (60.,90.): 'e', " +
                         "[90.,100.]: 'g'}")

        self.assertEqual(interval[(55.5, 70.5)], ["e", "c"])

        interval = Interval(0, 10)
        interval[(5.1, 5.5)] = "a"
        self.assertEqual(interval[(0, 10)], [None, "a"])
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,5.1): None, [5.1,5.5]: 'a', " +
                         "(5.5,10.]: None}")

        for i in np.arange(0.0, 10.0, 0.1).tolist():
            if i >= 5.1 and i <= 5.5:
                self.assertEqual(interval[i], "a")
            else:
                self.assertEqual(interval[i], None)

        interval[(5.6, 6.1)] = "b"
        self.assertEqual(interval[(0, 10)], [None, "a", "b"])
        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,5.1): None, [5.1,5.5]: 'a', " +
                         "(5.5,5.6): None, [5.6,6.1]: 'b', (6.1,10.]: None}")

        for i in np.arange(0.0, 10.0, 0.1).tolist():
            if i >= 5.1 and i <= 5.5:
                self.assertEqual(interval[i], "a")
            elif i >= 5.6 and i <= 6.1:
                self.assertEqual(interval[i], "b")
            else:
                self.assertEqual(interval[i], None)

        interval[(5.3, 5.8)] = "c"

        self.assertEqual(interval[(0, 10)], [None, "a", "b", "c"])
        self.assertEqual(interval[(5.3, 5.8)], ["c"])
        self.assertEqual(interval[(5.1, 5.9)], ["a", "b", "c"])
        self.assertEqual(interval[(5, 6)], [None, "a", "b", "c"])
        self.assertEqual(interval[(6, 7)], [None, "b"])
        self.assertEqual(interval[(5.05, 5.06)], [None])

        self.assertEqual(Interval.__str__(interval),
                         "Interval{[0.,5.1): None, [5.1,5.3): 'a', " +
                         "[5.3,5.8]: 'c', (5.8,6.1]: 'b', (6.1,10.]: None}")

        for i in np.arange(0.0, 10.0, 0.1).tolist():
            if i >= 5.1 and i < 5.3:
                self.assertEqual(interval[i], "a")
            elif i >= 5.3 and i <= 5.8:
                self.assertEqual(interval[i], "c")
            elif i > 5.8 and i <= 6.1:
                self.assertEqual(interval[i], "b")
            else:
                self.assertEqual(interval[i], None)


class test_interval_edge_cases(unittest.TestCase):

    def runTest(self):
        # Test default initialization (infinite range)
        interval = Interval()
        self.assertEqual(interval[0], None)
        self.assertEqual(interval[-1000], None)
        self.assertEqual(interval[1000], None)

        # Test initialization with integer values (should convert to float)
        interval = Interval(0, 10, "test")
        self.assertEqual(interval[5], "test")

        # Test __setitem__ with range completely before interval
        interval = Interval(10, 20)
        interval[(0, 5)] = "before"
        self.assertEqual(interval[15], None)  # Should not be set

        # Test __setitem__ with range completely after interval
        interval = Interval(10, 20)
        interval[(25, 30)] = "after"
        self.assertEqual(interval[15], None)  # Should not be set

        # Test __setitem__ with invalid range (xhi <= xlo)
        interval = Interval(10, 20)
        interval[(15, 15)] = "invalid"
        self.assertEqual(interval[15], None)  # Should not be set
        interval[(16, 15)] = "invalid2"
        self.assertEqual(interval[15], None)  # Should not be set

        # Test __setitem__ with range that clips to boundaries
        interval = Interval(10, 20)
        interval[(5, 25)] = "clipped"
        self.assertEqual(interval[10], "clipped")
        self.assertEqual(interval[15], "clipped")
        self.assertEqual(interval[20], "clipped")

        # Test __setitem__ when xhi already exists in xlist
        interval = Interval(0, 10)
        interval[(2, 5)] = "first"
        interval[(3, 5)] = "second"  # xhi already exists
        self.assertEqual(interval[4], "second")
        self.assertEqual(interval[5], "second")

        # Test __setitem__ when xlo already exists in xlist
        interval = Interval(0, 10)
        interval[(2, 5)] = "first"
        interval[(2, 7)] = "second"  # xlo already exists
        self.assertEqual(interval[3], "second")
        self.assertEqual(interval[6], "second")

        # Test __setitem__ when both endpoints already exist
        interval = Interval(0, 10)
        interval[(2, 5)] = "first"
        interval[(3, 4)] = "second"  # Both endpoints already exist
        self.assertEqual(interval[3.5], "second")

        # Test _index with x < xlist[0]
        interval = Interval(10, 20)
        with self.assertRaises(ValueError):
            interval._index(5)

        # Test _index with x > xlist[-1]
        interval = Interval(10, 20)
        with self.assertRaises(ValueError):
            interval._index(25)

        # Test _index with x > xlist[-2]
        interval = Interval(10, 20)
        idx = interval._index(19.5)
        self.assertEqual(idx, 0)  # Should return len(xlist) - 2 = 0

        # Test _index with x exactly at lower limit
        interval = Interval(10, 20)
        idx = interval._index(10)
        self.assertEqual(idx, 0)

        # Test _index with bias < 0 (choose lower range)
        interval = Interval(0, 10)
        interval[(5, 10)] = "upper"
        idx = interval._index(5, bias=-1)
        self.assertEqual(idx, 0)  # Should choose lower range

        # Test _index with bias > 0 (choose upper range)
        interval = Interval(0, 10)
        interval[(5, 10)] = "upper"
        idx = interval._index(5, bias=1)
        self.assertEqual(idx, 1)  # Should choose upper range

        # Test _index with bias == 0 and clo < chi (choose upper)
        interval = Interval(0, 10)
        interval[(2, 5)] = "first"   # count = 1
        interval[(3, 6)] = "second"  # count = 2, so clo (1) < chi (2)
        # At boundary 3, clo=1, chi=2, so should choose i (upper) when clo < chi
        idx = interval._index(3, bias=0)
        self.assertEqual(idx, 2)  # Should choose upper range (i=2)

        # Test _index with bias == 0 and clo > chi (choose lower)
        interval = Interval(0, 10)
        interval[(3, 6)] = "first"   # count = 1
        interval[(2, 5)] = "second"  # count = 2
        # Setting (2,5) removes boundary at 3, so x=3 is in range [2.0, 5.0) with index 1
        idx = interval._index(3, bias=0)
        self.assertEqual(idx, 1)  # Should be in range [2.0, 5.0)

        # Test __getitem__ with list type (not tuple)
        interval = Interval(0, 10)
        interval[(2, 5)] = "test"
        result = interval[[2, 5]]  # List instead of tuple
        self.assertIsInstance(result, list)
        self.assertIn("test", result)

        # Test __getitem__ with range that has duplicate values
        interval = Interval(0, 10)
        interval[(1, 3)] = "a"
        interval[(2, 4)] = "a"  # Duplicate value
        interval[(3, 5)] = "b"
        result = interval[(1, 5)]
        # Should have "a" only once, at the end due to deduplication
        self.assertEqual(result, ["a", "b"])

        # Test __getitem__ with single value at boundary
        interval = Interval(0, 10)
        interval[(5, 10)] = "upper"
        self.assertEqual(interval[5], "upper")
        self.assertEqual(interval[10], "upper")

        # Test __str__ with integer endpoints (should remove .0)
        interval = Interval(0, 10)
        interval[(5, 10)] = "test"
        str_repr = str(interval)
        self.assertIn("5", str_repr)
        self.assertIn("10", str_repr)
        # Should not have ".0" for integer endpoints
        self.assertNotIn("5.0", str_repr)
        self.assertNotIn("10.0", str_repr)

        # Test __str__ with float endpoints
        interval = Interval(0.5, 10.5)
        interval[(5.5, 10.5)] = "test"
        str_repr = str(interval)
        self.assertIn("5.5", str_repr)
        self.assertIn("10.5", str_repr)

        # Test __repr__
        interval = Interval(0, 10)
        interval[(5, 10)] = "test"
        repr_str = repr(interval)
        self.assertEqual(repr_str, str(interval))

        # Test complex overlapping scenario
        interval = Interval(0, 100)
        interval[(10, 20)] = "a"
        interval[(15, 25)] = "b"
        interval[(18, 22)] = "c"
        # At 19, should be "c" (most recent)
        self.assertEqual(interval[19], "c")
        # At 16, should be "b"
        self.assertEqual(interval[16], "b")
        # At 12, should be "a"
        self.assertEqual(interval[12], "a")

        # Test range query with multiple overlapping values
        result = interval[(10, 25)]
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertIn("c", result)
