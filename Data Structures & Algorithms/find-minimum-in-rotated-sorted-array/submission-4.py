import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # determine if middle pointer is in the left sorted or the right sorted.
        # the right sorted will contain the minimum value
        l, r = 0, len(nums) - 1
        min_so_far = nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            i = (l + r) // 2
            min_so_far = min(min_so_far, nums[i])
            if nums[i] >= nums[l]:
                # m is in the left sublist, so we want to search the right.
                min_so_far = min(min_so_far, nums[l])
                l = i + 1
            else:
                # m is in the right sublist, so we want to search to the left.
                min_so_far = min(min_so_far, nums[i])
                r = i - 1
        return min_so_far
        