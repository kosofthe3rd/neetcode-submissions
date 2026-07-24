class Solution:
    def numDecodings(self, s: str) -> int:
        mp = {}
        for i in range(1, 27):
            mp[str(i)] = chr(ord("A") + i - 1)
        print(mp)

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        print(dp)
         
        for i in range(1, len(s) + 1):
            if s[i-1 : i] in mp:
                dp[i] += dp[i - 1]
                print(dp)


            if i >= 2 and s[i-2:i] in mp:
                dp[i] += dp[i-2]
                print(dp)
                
        return dp[len(s)]