class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = sorted(s1)
        k = len(s1)
        l = 0
        if len(s2) < k:
            return False
        r = l + k - 1
        while r < len(s2):
            r = l + k - 1
            temp = s2[l : r + 1]
            if sorted(temp) == check:
                return True
            else:
                l += 1
        return False

        