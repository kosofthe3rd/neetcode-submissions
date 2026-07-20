class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        res = []

        for i in digits:
            s += str(i)
        
        t = int(s) + 1
        for i in str(t):
            res.append(i)
        return res
