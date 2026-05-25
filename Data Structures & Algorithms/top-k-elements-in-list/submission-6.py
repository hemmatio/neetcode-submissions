import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1 # key = number, value = # of occurrences

        for key, value in freq.items():
            print(f"key: {key}, value: {value}, result: {result}")
            result[value].append(key)

        final = []
        for i in range(len(result) -1, -1, -1):
            for n in result[i]:
                final.append(n)
                if len(final) == k:
                    return final

            


