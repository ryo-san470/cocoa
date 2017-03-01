# -*- coding: utf-8 -*-
class Factorize():
    def __init__(self, n):
        self.n = n

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


    def _isqrt(self, n):
        """
        Solve sqrt(n) in range of integer
        """
        x = n
        y = (x + 1) / 2
        while y < x:
            x = y
            y = (x + n/x) / 2
        return x
