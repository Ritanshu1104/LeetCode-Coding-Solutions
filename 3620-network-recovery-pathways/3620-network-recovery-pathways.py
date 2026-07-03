import heapq

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        unique_costs = sorted(list(set(e[2] for e in edges)))
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            
        def is_possible(min_edge_val):
            # Dijkstra to find the path with minimum total cost
            # while only using edges >= min_edge_val
            min_total_cost = [float('inf')] * n
            min_total_cost[0] = 0
            pq = [(0, 0)] # (current_total_cost, node)
            
            while pq:
                curr_dist, u = heapq.heappop(pq)
                if curr_dist > min_total_cost[u]: continue
                if u == n - 1: return curr_dist <= k
                
                for v, weight in adj[u]:
                    # Filter: Edge must meet the candidate score 
                    # and destination node (if intermediate) must be online
                    if weight >= min_edge_val:
                        if v == n - 1 or online[v]:
                            if min_total_cost[u] + weight < min_total_cost[v]:
                                min_total_cost[v] = min_total_cost[u] + weight
                                heapq.heappush(pq, (min_total_cost[v], v))
            return False

        # Binary search on the sorted unique edge costs
        ans = -1
        left, right = 0, len(unique_costs) - 1
        while left <= right:
            mid = (left + right) // 2
            if is_possible(unique_costs[mid]):
                ans = unique_costs[mid]
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
