class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        path = []

        

        def backprop(i):
            # goal: all nums reached
            if i >= len(nums):
                result.append(path.copy())
                return

            # choices: add number in nums, or don't
            path.append(nums[i])
            backprop(i + 1)
            path.pop()

            backprop(i + 1)

            # no constraints
        
        backprop(0)
        return result