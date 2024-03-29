import unittest
import soln1

class TestMethods(unittest.TestCase):
    def check_if_avail(self):
        self.assertTrue(soln1.check_if_available(0))
        self.assertTrue(soln1.check_if_available(10))
        self.assertTrue(soln1.check_if_available(9))
        self.assertFalse(soln1.check_if_available(4))

unittest.main()
