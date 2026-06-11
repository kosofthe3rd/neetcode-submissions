class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        temp = []
        res = []
        d_l = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def btrack(i):
            if i == len(digits):
                res.append("".join(temp))
                return
            
            cur = digits[i]
            letters = d_l[int(cur)]

            for letter in letters:
                temp.append(letter)
                btrack(i+1)
                temp.pop()
        
        btrack(0)

        return res

        


        
        