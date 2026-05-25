class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Have a list of used cells
        # First, check if my path length is equal to the word length
        # if it is, check each letter to see if it is equal
        # if it is not equal, backtrack
        # if it is not the same length (then it must be shorter)
        # so add one character
        # We need to go left, then pop, then right, then pop, then up, then pop, then down, then pop
        # When going in a certain direction, need to check to make sure it's not out of bounds.
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def DFS(r, c, pathlen):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[pathlen] or visited[r][c]:
                return False
            if len(word) - 1 == pathlen:
                return True

            visited[r][c] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                if DFS(r + dr, c + dc, pathlen + 1):
                    return True
            visited[r][c] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if DFS(r, c, 0):
                    return True
        return False
            

            
            