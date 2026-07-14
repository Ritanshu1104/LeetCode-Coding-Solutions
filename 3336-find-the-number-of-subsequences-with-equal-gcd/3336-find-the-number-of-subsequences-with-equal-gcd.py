from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the number of pairs with GCDs g1 and g2
        # We use 0 to represent an empty subsequence
        dp = {(0, 0): 1}
        
        for x in nums:
            new_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Choice 2: Add x to seq1
                new_g1 = gcd(g1, x) if g1 != 0 else x
                new_dp[(new_g1, g2)] = (new_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Choice 3: Add x to seq2
                new_g2 = gcd(g2, x) if g2 != 0 else x
                new_dp[(g1, new_g2)] = (new_dp.get((g1, new_g2), 0) + count) % MOD
            dp = new_dp
            
        # Sum counts where g1 == g2 and neither subsequence is empty
        ans = sum(count for (g1, g2), count in dp.items() if g1 == g2 and g1 != 0)
        return ans % MOD
