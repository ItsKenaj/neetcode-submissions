class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
            
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        path = set()
        def dfs(node, parent):
            if node in path:
                return False

            path.add(node)
            for neighbor in adj[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            
            return True
        
        return len(path) == n if dfs(0, -1) else False