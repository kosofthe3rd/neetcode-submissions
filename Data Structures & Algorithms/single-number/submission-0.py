class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        num = Counter(nums)

        for n, freq in num.items():
            if freq == 1:
                return n
        