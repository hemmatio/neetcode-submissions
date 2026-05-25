class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        

        def dfs(r, c):
            if not ((0 <= r <= len(grid) - 1) and (0 <= c <= len(grid[0]) - 1)):
                return
            if grid[r][c] == '0' or visited[r][c] == True:
                return
            visited[r][c] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        islandcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited[r][c]:
                    islandcount += 1
                    dfs(r, c)

        return islandcount

