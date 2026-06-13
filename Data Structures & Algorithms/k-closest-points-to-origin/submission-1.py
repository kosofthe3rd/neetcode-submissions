import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in points:
            heapq.heappush(heap, [self.euclid_dist(i), i])
        heapq.heapify(heap)

        res = []

        while len(res) < k:
            dist, i = heapq.heappop(heap)
            res.append(i)
        
        return res

    
    def euclid_dist(self, point):
        return (point[0]**2) + (point[1]**2)