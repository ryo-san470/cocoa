import unittest
from cocoa.factorize import Factorize


class TestFactorizeTestCase(unittest.TestCase):
    def test_trial_division(self):
        p = 577
        q = 709

        f = Factorize(p * q)
        solve_p = f.trial_division()

        self.assertEqual(p, solve_p)
