import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        count = []
        time = 0
        count = [- e for e in frequency.values()]
        heapq.heapify(count)
        cooldown = deque()
        while count or cooldown:
            time += 1
            if count:
                cnt = 1 + heapq.heappop(count)
                if cnt:
                    cooldown.append([cnt, time + n])
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(count, cooldown.popleft()[0])
        
        return time
                

