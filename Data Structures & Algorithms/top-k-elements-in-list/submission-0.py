import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = []
        for c, i in sorted(hashmap.items(), key=lambda x: x[1], reverse=True):
            print([c, i])
            if k > 0:
                res.append(c)
                k -= 1
            else:
                break
        return res

        



        