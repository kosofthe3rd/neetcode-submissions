class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_map = set()
        for i in nums:
            if i not in seen_map:
                seen_map.add(i)
            else:
                return True
        return False

        