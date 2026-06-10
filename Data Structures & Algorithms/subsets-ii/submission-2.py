class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashset = {}
        temp = []
        res = []
        count = 0
        def dfs(i):
            nonlocal count
            if i == len(nums):
                if temp.copy() not in hashset.values():
                    hashset[count] = temp.copy()
                    res.append(temp.copy())
                    count += 1
                return
            temp.append(nums[i])
            dfs(i + 1)
            temp.pop()
            dfs(i + 1)
        dfs(0)
        return res
            