import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            print(i)
            dist = self.euclid_distance(i)
            heapq.heappush(heap, [dist, i])
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            dist, i = heapq.heappop(heap)
            res.append(i)
        return res
    def euclid_distance(self, point):
        return (point[0])** 2 + (point[1])**2