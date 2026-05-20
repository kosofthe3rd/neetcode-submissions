class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = ""
        res2 = ""
        for i in s:
            if i.isalnum():
                res1 += i.lower()
            else:
                continue
        for i in range(len(res1)-1, -1, -1):
            res2 += res1[i]
        
        return res2 == res1