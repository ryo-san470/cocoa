# -*- coding: utf-8 -*-
from fractions import gcd
from Crypto.Random.random import randint
# from Crypto.Util.number import GCD

from timeout_decorator import timeout, TimeoutError


class Factorize():
    def __init__(self, n, wait=5):
        self.n = n
        self.wait = wait

    def trial_division(self):
        k = self._isqrt(self.n)

        if self.n % 2 == 0:
            return 2
        if self.n % 3 == 0:
            return 3

        i = 6
        while i < k:
            if self.n % (i - 1) == 0:
                return i - 1
            if self.n % (i + 1) == 0:
                return i + 1
            i += 6

    def pollard_rho(self):
        """
        Pollard Rho methods O(p^(1/2)) <= O(n^(1/4))
        """
        is_prime = self._miller_rabin()

        if is_prime:
            return None
        else:
            x, y, d = 2, 2, 1

            while d == 1:
                x = (x*x + 1) % self.n
                y = (y*y + 1) % self.n
                y = (y*y + 1) % self.n
                d = gcd(abs(x-y), self.n)

            if d != self.n:
                return d

    def fermat(self):
        """
        Fermat factorization method
        https://en.wikipedia.org/wiki/Fermat's_factorization_method
        """
        @timeout(self.wait)
        def inner(n):
            p = self._fermat(n)
            return p
        try:
            return inner(self.n)
        except:
            return None

    def _isqrt(self, n):
        """
        Solve sqrt(n) in range of integer
        """
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n//x) // 2
        return x

    def _miller_rabin(self, k=20):
        """Miller Rabin primality set"""
        s, d = 0, self.n - 1

        while d % 2 == 0:
            s += 1
            d //= 2

        for i in range(k):
            a = randint(2, self.n - 1)
            x = pow(a, d, self.n)
            if x == 1:
                continue
            for r in range(s):
                if x == self.n - 1:
                    break
                x = (x * x) % self.n
            else:
                return False

        return True

    def _is_square(self, n):
        if not n % 48 in (0, 1, 4, 9, 16, 25, 33, 36):
            return False

        x = self._isqrt(n)
        return x*x == n

    def _fermat(self, n):
        a = self._isqrt(n)
        b2 = a*a - n
        while not self._is_square(b2):
            a += 1
            b2 = a*a - n
        return a - self._isqrt(b2)
