import heapq
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num * -1)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)

    def findMedian(self) -> float:
        if (len(self.large) + len(self.small)) % 2 == 0:
            return (self.large[0] + self.small[0] * -1) / 2.0
        else:
            if len(self.large) > len(self.small):
                return self.large[0]
            else:
                return self.small[0] * -1
        
         