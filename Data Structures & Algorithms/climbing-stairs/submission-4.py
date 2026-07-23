class Solution:
    def climbStairs(self, n: int) -> int:

        res = [1 for _ in range(n + 1)]
        print(res)
        if n <= 2:
            return n
        if n > 2:
            for i in range(len(res)-3, -1, -1):

                res[i] = res[i + 2] + res[i + 1]
        
        return res[0]