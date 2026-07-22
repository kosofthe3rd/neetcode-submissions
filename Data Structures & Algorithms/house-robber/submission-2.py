class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0 for _ in range(len(nums) + 2)]

        for i in range(len(nums)-1, -1, -1):
            skip_next = nums[i] + dp[i + 2]
            skip_cur = dp[i+1]

            dp[i] = max(skip_cur, skip_next)

        
        return dp[0]
