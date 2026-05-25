from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # create two graphs: Visited Pacific, Visited Atlantic
        # Start from the water-bordering blocks, and add to queue
        # From the water borders, move upwards to anything that is higher. 
        # If an adjacent is higher, that means that it does reach that water
        # do two passes, and then return the intersections.

        visited_pac = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        visited_atl = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]

        pac_queue = deque()
        atl_queue = deque()

        for c in range(len(heights[0])):
            visited_pac[0][c] = True
            pac_queue.append((0,c))

        for r in range(len(heights)):
            visited_pac[r][0] = True
            pac_queue.append((r, 0))
        
        for c in range(len(heights[0])):
            visited_atl[-1][c] = True
            atl_queue.append((len(heights) - 1, c))

        for r in range(len(heights)):
            visited_atl[r][-1] = True
            atl_queue.append((r, len(heights[0]) - 1))

        # pass 1: pac
        while pac_queue:
            r, c = pac_queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= len(heights) - 1 and 0 <= nc <= len(heights[0]) - 1:
                    if heights[nr][nc] >= heights[r][c] and not visited_pac[nr][nc]:
                        visited_pac[nr][nc] = True
                        pac_queue.append((nr, nc))

        while atl_queue:
            r, c = atl_queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= len(heights) - 1 and 0 <= nc <= len(heights[0]) - 1:
                    if heights[nr][nc] >= heights[r][c] and not visited_atl[nr][nc]:
                        visited_atl[nr][nc] = True
                        atl_queue.append((nr, nc))

        intersections = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if visited_atl[r][c] and visited_pac[r][c]:
                    intersections.append([r, c])
        
        return intersections
