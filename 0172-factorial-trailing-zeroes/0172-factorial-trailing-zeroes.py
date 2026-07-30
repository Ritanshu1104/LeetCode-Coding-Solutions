class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = n // 5
        ans += n // 25
        ans += n //125
        ans += n // 625
        ans += n // 3125
        
        
        return ans