
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        lp = 0 
        curr_sum = 0
        for rp in range(len(nums)):
            curr_sum += nums[rp]
            while curr_sum >= target:
                min_length = min(min_length, rp - lp + 1)
                curr_sum -= nums[lp]
                lp += 1          
            
        if min_length > len(nums):
            return 0
        return min_length

        