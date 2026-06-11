class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        count = 0
        def backtrack(r, c, count):
            if count == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[count]):
                return False

            temp = board[r][c] 
            board[r][c] = "#"  
            found = ( 
                backtrack(r + 1, c, count + 1) or
                backtrack(r - 1, c, count + 1) or
                backtrack(r, c + 1, count + 1) or
                backtrack(r, c - 1, count + 1)
            )
            board[r][c] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False



