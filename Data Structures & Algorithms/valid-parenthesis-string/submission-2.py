class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            l, s = left.pop(), star.pop()
            if l > s:
                return False
            else:
                continue
        return not left
