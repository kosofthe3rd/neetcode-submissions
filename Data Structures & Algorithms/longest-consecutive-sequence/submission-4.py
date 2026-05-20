class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        best = 1
        for n in nums:
            if n - 1 not in nums_set:
                length = 1
                while n + length in nums_set:
                    length += 1
                    best = max(best, length)
        
        return best