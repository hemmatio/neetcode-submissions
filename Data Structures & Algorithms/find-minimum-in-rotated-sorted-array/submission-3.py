import math
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        # If the array is not rotated (already sorted), the first element is the minimum.
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half of the array.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum element must be in the left half (including mid).
            else:
                right = mid

        # At the end of the loop, left and right will point to the minimum element.
        return nums[left]