class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp = []
        res = []
        def dfs(i):
            if sum(temp) == target:
                res.append(temp.copy())
                return
            if sum(temp) > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                temp.append(candidates[j])
                dfs(j + 1)
                temp.pop()
        dfs(0)
        return res