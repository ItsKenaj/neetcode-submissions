class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        cycleStart = -1
        visited = [False] * (n + 1)
        def dfs(node, prev):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True
            for nei in adj[node]:
                if nei != prev:
                    if dfs(nei, node):
                        if cycleStart != -1:
                            cycle.add(nei)
                        if node == cycleStart:
                            cycleStart = -1
                        return True
            return False
        
        dfs(1, -1)
        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1, n2]

        return []

    