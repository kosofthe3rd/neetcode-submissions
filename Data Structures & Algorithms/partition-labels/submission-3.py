class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        intervals = []
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [i, i]
            else:
                hashmap[s[i]][1] = i

        for c in hashmap.values():
            intervals.append(c)
        
        res = []

        start, end = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if end > intervals[i][0]:
                end = max(end, next_end)
            else:
                res.append((end - start) + 1)
                start, end = next_start, next_end
        
        res.append(end - start + 1)
        return res
