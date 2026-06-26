class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Offset to handle negative indices in the Fenwick Tree
        offset = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        # Initial prefix sum is 0
        current_sum = 0
        update(current_sum + offset, 1)
        
        ans = 0
        for x in nums:
            if x == target:
                current_sum += 1
            else:
                current_sum -= 1
            
            # Count prefix sums strictly less than current_sum
            ans += query(current_sum + offset - 1)
            update(current_sum + offset, 1)
            
        return ans
