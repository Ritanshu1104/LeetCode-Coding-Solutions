from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Sparse Tables
        LOG = n.bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            mx_row = []
            mn_row = []

            for i in range(n - length + 1):
                mx_row.append(max(mx[j - 1][i],
                                  mx[j - 1][i + half]))
                mn_row.append(min(mn[j - 1][i],
                                  mn[j - 1][i + half]))

            mx.append(mx_row)
            mn.append(mn_row)
            j += 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1

            mxv = max(mx[p][l], mx[p][r - (1 << p) + 1])
            mnv = min(mn[p][l], mn[p][r - (1 << p) + 1])

            return mxv - mnv

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            if r > l:
                nr = r - 1
                nv = value(l, nr)
                heapq.heappush(heap, (-nv, l, nr))

        return ans