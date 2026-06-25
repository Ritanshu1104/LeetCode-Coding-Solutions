class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Offset to handle negative prefix sums in an array-based frequency map
        # Max possible range of prefix sum is [-n, n]
        offset = n 
        counts = [0] * (2 * n + 1)
        
        prefix_sum = 0
        counts[offset] = 1 # Represents prefix sum 0 before starting
        
        result = 0
        smaller_sums_count = 0
        
        for num in nums:
            # Transform: target is 1, others are -1
            if num == target:
                # Moving from sum to sum+1
                # We gain the count of the previous sum level
                smaller_sums_count += counts[prefix_sum + offset]
                prefix_sum += 1
            else:
                # Moving from sum to sum-1
                # We lose the count of the new sum level
                prefix_sum -= 1
                smaller_sums_count -= counts[prefix_sum + offset]
            
            result += smaller_sums_count
            counts[prefix_sum + offset] += 1
            
        return result
