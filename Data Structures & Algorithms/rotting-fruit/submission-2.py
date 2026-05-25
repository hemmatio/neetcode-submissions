from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        num_fresh = 0
        minutes = 0

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        while queue:
            size_of_level = len(queue)
            for _ in range(size_of_level):
                r, c = queue.popleft() # rotten fruit
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    if 0 <= r + dr <= len(grid) - 1 and 0 <= c + dc <= len(grid[0]) - 1 and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        num_fresh -= 1
                        queue.append((r + dr, c + dc)) # add fresh fruit to queue
            if queue: # We need another minute, because there is fresh fruit in queue
                minutes += 1

        if num_fresh == 0:
            return minutes
        return -1

