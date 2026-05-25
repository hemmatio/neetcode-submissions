class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # if we already looked at this number
                continue
            needed = -1 * nums[i]
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if nums[p1] + nums[p2] == needed:
                    solutions.append([nums[p1], nums[p2], -1 * needed])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif needed > nums[p1] + nums[p2]:
                    p1 += 1
                else:
                    p2 -= 1
                
        return solutions

        