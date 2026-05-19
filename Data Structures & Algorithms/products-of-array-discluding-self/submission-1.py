class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1 for _ in range(len(nums))]

        l, r = 1, 1
        for i in range(len(nums)):
            product[i] = l
            l *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            product[i] *= r
            r *= nums[i]
        return product