class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []
        for i in range(len(position)):
            arr.append([position[i], (target - position[i])/speed[i]])
        arr.sort(reverse=True)
        for pos, time in arr:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)