class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one_prev, two_prev = 0, 0

        for c in cost:
            cur = c + min(one_prev, two_prev)
            two_prev, one_prev = one_prev, cur
        
        return min(two_prev, one_prev)

