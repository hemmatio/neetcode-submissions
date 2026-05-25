import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1 
            if x < y:
                heapq.heappush(heap, (y - x) * -1)
            elif x > y:
                heapq.heappush(heap, (x - y) * -1)
        if len(heap) == 1:
            return heapq.heappop(heap) * -1
        return 0
