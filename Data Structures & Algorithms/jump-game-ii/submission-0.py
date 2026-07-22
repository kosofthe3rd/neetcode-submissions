class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        step = 0
        while r < len(nums)-1:
            l, r = r + 1, r + max(nums[l: r + 1])
            step += 1
            print(l, r)
        return step



