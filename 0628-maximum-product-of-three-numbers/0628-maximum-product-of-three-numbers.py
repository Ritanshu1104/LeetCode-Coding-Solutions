class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        h, l = [], []

        for n in nums:
            heapq.heappush(h, n)
            if len(h) > 3:
                heapq.heappop(h)

            heapq.heappush(l, -n)
            if len(l) > 2:
                heapq.heappop(l)

        h3 = heapq.heappop(h)
        h2 = heapq.heappop(h)
        h1 = heapq.heappop(h)

        l2 = -heapq.heappop(l)
        l1 = -heapq.heappop(l)

        return max(h1 * h2 * h3, h1 * l1 * l2)