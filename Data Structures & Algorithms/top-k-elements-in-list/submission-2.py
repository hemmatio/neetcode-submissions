import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heapq.heapify(result)
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1


        for key, value in freq.items():
            heapq.heappush_max(result, (value, key))

        final = []
        for _ in range(k):
            final.append(heapq.heappop_max(result)[1])
        return final

            


