import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        time = 0
        count = [- e for e in freq.values()]
        heapq.heapify(count)
        cooldown = deque()

        while cooldown or count:
            time += 1
            if count:
                cnt = 1 + heapq.heappop(count)
                if cnt:
                    cooldown.append([cnt, time + n])
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(count, cooldown.popleft()[0])
        
        return time


