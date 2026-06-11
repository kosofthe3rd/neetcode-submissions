class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def btrack(i):
            if i == len(s):
                res.append(temp.copy())
                return
            
            word = ""
            
            for j in range(i, len(s)):
                word += s[j]
                if self.isPalindrome(word):
                    temp.append(word)
                    btrack(j + 1)
                    temp.pop()
        
        btrack(0)
        return res


        
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n):
            if s[i] != s[n - (i + 1)]:
                return False
                break
        return True
            
            


