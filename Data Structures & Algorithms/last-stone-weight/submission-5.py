import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for i in stones:
            heapq.heappush(heap, -i)
        print(heap)
        while len(heap) > 1:
            l1 = heapq.heappop(heap)
            l2 = heapq.heappop(heap)
            val = abs(l1 - l2)
            if val > 0:
                heapq.heappush(heap, -val)
            if val == 0:
                continue
        if not heap:
            return 0
        
        return -1 * heap[0]
    

        