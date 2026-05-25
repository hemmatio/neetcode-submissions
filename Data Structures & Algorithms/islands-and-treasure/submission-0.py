from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Now the queue contains all of the treasure chests.

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(queue) > 0:
            coords = queue.popleft()
            r, c = coords[0], coords[1]
            for dr, dc in directions:
                if 0 <= r + dr <= len(grid) - 1 and 0 <= c + dc <= len(grid[0]) - 1:
                    if grid[r + dr][c + dc] == 2147483647:
                        grid[r + dr][c + dc] = grid[r][c] + 1
                        queue.append((r + dr, c + dc))

            

