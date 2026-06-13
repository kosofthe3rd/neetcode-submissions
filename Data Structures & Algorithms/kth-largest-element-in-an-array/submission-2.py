class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest element in a size n is the k - n smallest element
        n = len(nums)
        heap = []
        heapq.heapify(heap)

        for i in nums:
            heapq.heappush(heap, i)

        for _ in range(n - k):
            heapq.heappop(heap)

        return heap[0]
        
