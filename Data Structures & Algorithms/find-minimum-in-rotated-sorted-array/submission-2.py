import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # determine if middle pointer is in the left sorted or the right sorted.
        # the right sorted will contain the minimum value
        l, r = 0, len(nums) - 1
        min_so_far = math.inf
        while l <= r:
            m = ((r - l) // 2) + l
            if nums[l] < nums[r]:
                # we are in a normally sorted section:
                return min(min_so_far, nums[l])
                
            elif nums[m] >= nums[l]:
                # m is in the left sublist, so we want to search the right.
                l = m + 1
            else:
                # m is in the right sublist, so we want to search to the left.
                r = m - 1
            min_so_far = min(min_so_far, nums[m])
        return min_so_far
        