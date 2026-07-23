class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        arr_1 = nums[:-1]
        arr_2 = nums[1:]

        def run_max(arr):
            dp = [0 for _ in range(len(arr) + 2)]
            print(dp, arr)
            for i in range(len(arr)-1, -1, -1):
                print(i)
                skip_next = arr[i] + dp[i + 2]
                skip_cur = dp[i + 1]

                dp[i] = max(skip_cur, skip_next)
                print(dp, arr)
            return dp[0]

        return max(run_max(arr_1), run_max(arr_2))