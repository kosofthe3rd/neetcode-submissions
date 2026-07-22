class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0

        while r < len(nums)-1:
            l, r = r + 1, max(i + nums[i] for i in range(l, r + 1))
            steps += 1
        
        return steps