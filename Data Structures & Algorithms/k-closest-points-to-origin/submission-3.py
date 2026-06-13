import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in points:
            heapq.heappush(heap, [(i[0]**2) + (i[1]**2), i])
        
        res = []
        while len(res) < k:
            dist, i = heapq.heappop(heap)
            res.append(i)
        
        return res
