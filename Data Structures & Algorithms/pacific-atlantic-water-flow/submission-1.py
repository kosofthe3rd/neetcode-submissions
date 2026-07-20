class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])

        
        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                ro, co = r + dr, c + dc

                if ( 0 <= ro < rows and 0 <= co < cols and (ro, co) not in visited and heights[ro][co] >= heights[r][c]):
                    dfs(ro, co, visited)
        
        for c in range(len(heights[0])):
            dfs(0, c, pac)
            dfs(len(heights) - 1, c, atl)
        
        for r in range(len(heights)):
            dfs(r, 0, pac)
            dfs(r, len(heights[0]) - 1, atl)
        
        return list(pac & atl)