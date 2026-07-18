class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        not_sur = set()
        q = deque()

        def bfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in not_sur or board[r][c] == "X"):
                return
            not_sur.add((r, c))
            q.append([r, c])

        for r in range(rows):
            if board[r][-1] == "O":
                not_sur.add((r, len(board[0]) - 1))
                q.append([r, len(board[0]) - 1])
            if board[r][0] == "O":
                not_sur.add((r, 0))
                q.append([r, 0])
        for c in range(cols):
            if board[0][c] == "O":
                not_sur.add((0, c))
                q.append([0, c])
            if board[-1][c] == "O":
                not_sur.add((len(board)-1, c))
                q.append([len(board)-1, c])
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                board[r][c] = "#"
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "#":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"


