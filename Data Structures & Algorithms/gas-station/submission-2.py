class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        tank = [0 for _ in range(len(cost))]
        index = [False for _ in range(len(cost))]

        def circuit(i):
            n = 0
            temp = 0

            while n < len(gas):
                station = (i + n) % len(gas)
                temp += gas[station] - cost[station]
                n += 1

                if temp < 0:
                    tank[i] = temp
                    return
            
            tank[i] = temp
            index[i] = True
        
        for i in range(len(gas)):
            circuit(i)

        print(tank)
        for i, val in enumerate(index):
            if val:
                return i
        return -1
        




        

        

