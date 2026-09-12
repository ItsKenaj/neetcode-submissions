class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for node in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for nei in adj[node]:
                dfs(nei)
        
        for node in range(n):
            if len(visited) == n:
                return components

            if node in visited:
                continue

            components += 1
            dfs(node)
            
        return components
