class Solution:
    def rob(self, nums: List[int]) -> int:

        arr_1 = nums[0:-1]
        arr_2 = nums[1:]
        
        if len(nums) <= 2:
            return max(nums) 
        def run_max(arr):
            dp = [0 for _ in range(len(arr)+2)]
            for i in range(len(arr)-1, -1, -1):
                skip_next = arr[i] + dp[i+2]
                skip_cur = dp[i + 1]

                dp[i] = max(skip_next, skip_cur)
            
            return dp[0]
        
        print(arr_1, arr_2)
        print(run_max(arr_1), run_max(arr_2))
        return max(run_max(arr_1), run_max(arr_2))

            
