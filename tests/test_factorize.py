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

    def test_fermat_success(self):
        r = self._import_public_key("fermat.pem")
        f = Factorize(r.n)
        solve_p = f.fermat()
        solve_q = r.n // solve_p

        self.assertEqual(r.n, solve_p * solve_q)

    def test_fermat_timeout(self):
        r = self._import_public_key("1024.pem")
        f = Factorize(r.n, wait=2)
        solve_p = f.fermat()

        self.assertEqual(solve_p, None)

    def test_small_prime(self):
        r = self._import_public_key("small_prime.pem")
        f = Factorize(r.n)
        solve_p = f.small_prime()

        self.assertNotEqual(solve_p, None)
        solve_q = r.n // solve_p

        self.assertEqual(r.n, solve_p * solve_q)

    def _import_public_key(self, pem):
        import os.path
        root = os.path.dirname(os.path.abspath(__file__))

        from Crypto.PublicKey import RSA
        r = RSA.importKey(open(os.path.join(root, "pems", pem)).read())
        return r


