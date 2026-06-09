class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        res = []
        def dfs(i):
            if sum(temp) == target:
                res.append(temp.copy())
                return
            if i == len(nums) or sum(temp) > target:
                return
            temp.append(nums[i])
            dfs(i)
            temp.pop()
            dfs(i + 1)
        dfs(0)
        return res