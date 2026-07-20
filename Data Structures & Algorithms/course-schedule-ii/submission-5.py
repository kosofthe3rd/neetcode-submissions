class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = defaultdict(list)
        completed = set()
        visited = set()

        res = []

        for c, p in prerequisites:
            if c not in pre_req:
                pre_req[c] = [p]
            else:
                pre_req[c].append(p)
        
        def dfs(c):
            if c in completed:
                return True
            
            if c in visited:
                return False
            
            if not pre_req[c]:
                completed.add(c)
                res.append(c)
                return True
            
            visited.add(c)

            for pre in pre_req[c]:
                if not dfs(pre):
                    return False

            visited.remove(c)
            completed.add(c)
            res.append(c)
            pre_req[c] = []
            return True
                

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res