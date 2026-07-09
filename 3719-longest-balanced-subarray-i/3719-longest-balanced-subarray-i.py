class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        length = 0

        # Try all subarrays starting at i
        for i in range(n):
            odd = set()
            even = set()

            for j in range(i, n):
                # classify current element
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                # check balance condition
                if len(odd) == len(even):
                    length = max(length, j - i + 1)

        return length