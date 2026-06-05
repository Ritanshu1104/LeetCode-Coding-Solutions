from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @cache
            def dp(pos, tight, started, prev2, prev1, waves):
                if pos == len(s):
                    return waves

                limit = int(s[pos]) if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        ans += dp(pos + 1, ntight, False, -1, -1, waves)
                    else:
                        nwaves = waves

                        if started and prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or \
                               (prev1 < prev2 and prev1 < d):
                                nwaves += 1

                        if not started:
                            ans += dp(pos + 1, ntight, True, -1, d, nwaves)
                        elif prev2 == -1:
                            ans += dp(pos + 1, ntight, True, prev1, d, nwaves)
                        else:
                            ans += dp(pos + 1, ntight, True, prev1, d, nwaves)

                return ans

            return dp(0, True, False, -1, -1, 0)

        return solve(num2) - solve(num1 - 1)