class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(set)
        visited = set()
        for c, p in prerequisites:
            if c not in pre_req:
                pre_req[c] = [p]
            else:
                pre_req[c].append(p)
        
        def dfs(c):
            if c in visited:
                return False
            if not pre_req[c]:
                return True
            
            visited.add(c)
            for pre in pre_req[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            pre_req[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True