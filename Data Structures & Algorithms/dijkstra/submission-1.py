import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for s, dest, weight in edges:
            adj[s].append([dest, weight])
        
        shortest = {}
        pqueue = [[0, src]]
        while pqueue:
            w1, n1 = heapq.heappop(pqueue)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(pqueue, [w1 + w2, n2])
        

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        
        return shortest

