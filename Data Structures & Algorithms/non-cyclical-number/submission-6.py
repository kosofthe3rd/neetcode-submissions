class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def convert_calc(i):
            val = 0
            s = str(i)
            for i in s:
                val += int(i) * int(i)
            return val

        res = convert_calc(n)
        while res != 1:
            res = convert_calc(res)
            if res in seen:
                return False
            else:
                seen.add(res)
        return True
            
        