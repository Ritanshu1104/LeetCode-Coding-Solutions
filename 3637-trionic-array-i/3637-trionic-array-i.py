class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        i = 0
        
        # 1. Strictly increasing to peak p
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        
        p = i
        # p cannot be at the start (must have increased) or at the end
        if p == 0 or p == n - 1:
            return False
            
        # 2. Strictly decreasing to valley q
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            
        q = i
        # q must be greater than p and cannot be at the end
        if q == p or q == n - 1:
            return False
            
        # 3. Strictly increasing to the end
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # If we reached the last index, it's trionic
        return i == n - 1
