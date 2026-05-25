class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #n1 + n2 + n3 = 0 ==> -n1 = n2 + n3
            needed = -1 * nums[i]
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                s = nums[p1] + nums[p2]
                if s > needed:
                    p2 -= 1
                elif s < needed:
                    p1 += 1
                elif s == needed:
                    triplets.append([nums[p1], nums[p2], nums[i]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
        return triplets
                    
