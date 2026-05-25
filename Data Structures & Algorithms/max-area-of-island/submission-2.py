class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        visited = [[False for _ in grid[0]] for _ in grid]
        
        def area(r, c):
            nonlocal maxarea
            if not (0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1):
                return 0
            if visited[r][c] or grid[r][c] == 0:
                return 0

            currarea = 1   
            visited[r][c] = True

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dr, dc in directions:
                currarea += area(r + dr, c + dc)
            return currarea
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    maxarea = max(maxarea, area(r, c))

        return maxarea

