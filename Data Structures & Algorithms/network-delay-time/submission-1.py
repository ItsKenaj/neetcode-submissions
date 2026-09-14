import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for n1, n2, wt in times:
            edges[n1].append((n2, wt))
        
        time = 0
        pqueue = [(0, k)]
        visited = set()
        while pqueue:
            w1, n1 = heapq.heappop(pqueue)
            if n1 in visited:
                continue
            
            visited.add(n1)
            time = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(pqueue, (w1 + w2, n2))
        
        return time if len(visited) == n else -1