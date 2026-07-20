class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashmap = {"0" : 0 , "1" : 1, "2" : 2, "3" : 3, "4" : 4,
                   "5": 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        
        def conv(s):
            res = 0
            for i in range(len(s)-1, -1, -1):
                res += hashmap[s[i]] * (10)**(len(s) - (i + 1))
            return res
        print(conv(num1), conv(num2))
        return str(conv(num1) * conv(num2))
        

        
        