class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        found = [False, False, False]
        hashmap = {target[0]: 1, target[1]:1, target[2]: 1}
        print(hashmap)
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            
            for i in range(3):
                if trip[i] == target[i]:
                    found[i] = True
        
        return all(found)


            



        