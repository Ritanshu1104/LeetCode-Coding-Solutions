import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        k = r-l+1
        f0 = np.zeros((k, 1), dtype=object)
        f0[-1] = 1
        A = (np.arange(k)[::-1][:, None] < np.arange(k)).astype(object)
        def exp(A, n):
            if n == 0: return np.identity(k, dtype=object)
            if n%2: return exp(A, n-1) @ A % mod
            return exp(A @ A % mod, n//2)
        An = exp(A, n)
        fn = An @ f0
        return np.sum(fn)*2 % mod