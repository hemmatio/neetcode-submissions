class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            needed = target - nums[i] 
            idx = map.get(needed)
            if idx and idx != i:
                return [i, idx]
