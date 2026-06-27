from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 1
        
        # Handle 1s specifically (must be odd length)
        if 1 in count:
            res = count[1] if count[1] % 2 == 1 else count[1] - 1
            
        for x in count:
            if x == 1: continue
            
            curr_len = 0
            curr = x
            
            # Build the sequence x, x^2, x^4...
            while curr in count and count[curr] >= 2:
                curr_len += 2
                curr = curr * curr
                
            # Add the peak element
            if curr in count:
                curr_len += 1
            else:
                curr_len -= 1
                
            res = max(res, curr_len)
            
        return res
