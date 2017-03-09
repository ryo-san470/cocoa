import unittest
from Crypto.Util.number import getPrime
from cocoa.factorize import Factorize


class TestFactorizeTestCase(unittest.TestCase):
    def setUp(self):
        self.p = getPrime(24)
        self.q = getPrime(24)
        self.n = self.p * self.q

    def test_trial_division(self):
        f = Factorize(self.n)
        solve_p = f.trial_division()

        p = self.p if self.p < self.q else self.q
        self.assertEqual(p, solve_p)

    def test_pollard_rho(self):
        f = Factorize(self.n)
        solve_p = f.pollard_rho()
        solve_q = self.n // solve_p

        self.assertEqual(self.n, solve_p * solve_q)
