from math import sqrt
from collections import defaultdict
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getdist(point):
            x = point[0]
            y = point[1]
            dist = sqrt((x ** 2) + (y ** 2))
            return dist
        

        distheap = []
        heapq.heapify(distheap)
        disttopoints = defaultdict(list)

        for point in points:
            dist = getdist(point)
            disttopoints[dist].append(point)
            heapq.heappush(distheap, dist)

        res = []
        while len(res) < k:
            closestdist = heapq.heappop(distheap)
            res.extend(disttopoints[closestdist])

        return res[:k]
