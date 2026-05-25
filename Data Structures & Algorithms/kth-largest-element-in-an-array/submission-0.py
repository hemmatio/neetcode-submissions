import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        for _ in range(k):
            returnval = heapq.heappop(nums)
        return returnval * -1