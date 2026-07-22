class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        def circuit(i):
            n = 0
            temp = 0

            while n < len(gas):
                station = (i + n) % len(gas)
                temp += gas[station] - cost[station]
                n += 1

                if temp < 0:
                    return False
            
            return True
        
        for i in range(len(gas)):
            if circuit(i):
                return i
        return - 1



        

        

