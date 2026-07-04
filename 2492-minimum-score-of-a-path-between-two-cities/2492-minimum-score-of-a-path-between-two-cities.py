class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create adjacency list: node -> list of (neighbor, distance)
        adj = collections.defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        
        min_score = float('inf')
        visited = set()
        queue = collections.deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            
            for neighbor, dist in adj[node]:
                # Update min_score with every road in the component
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
