class Solution:
    def myPow(self, x: float, n: int) -> float:

        temp = x
        if n > 0:
            while n > 1:
                x *= temp
                n -= 1
        else:
            while n < 1:
                x /= temp
                n += 1
        return x

