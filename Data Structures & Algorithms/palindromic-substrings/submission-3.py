class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 

        def check_pal(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        for i in range(len(s)):
            l, r = i, i
            res += check_pal(l, r)

            l, r = i, i + 1
            res += check_pal(l, r)


        return res