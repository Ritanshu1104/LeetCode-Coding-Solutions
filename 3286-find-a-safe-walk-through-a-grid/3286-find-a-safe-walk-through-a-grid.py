from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        # Track minimum health lost to reach each cell
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Starting cell cost
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            
            # If we reached the end, check if we have at least 1 health left
            if r == m - 1 and c == n - 1:
                return dist[r][c] < health
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = dist[r][c] + grid[nr][nc]
                    # If we found a "cheaper" path to this cell
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        # 0-1 BFS logic
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
                            
        return False
