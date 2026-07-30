class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        max_res = nums[0]

        for i in nums[1::]:
            prev_max = cur_max

            cur_max = max(i, i * cur_max, i * cur_min)
            cur_min = min(i, i * prev_max, i * cur_min)
            

            max_res = max(max_res, cur_max)
        
        return max_res
