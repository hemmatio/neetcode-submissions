class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # keep track of the combinations
        combinations = []
        def trycomb(i, currcomb, currsum):
            # found a match
            if currsum == target:
                combinations.append(currcomb.copy())
                return 
            # past the index
            if i >= len(nums):
                return
            # if we can't add, return
            elif currsum + nums[i] > target:
                trycomb(i + 1, currcomb, currsum)
                return
            # add nums[i], try adding again, then try adding next
            currcomb.append(nums[i])
            trycomb(i, currcomb, currsum + nums[i])
            # we are done with i, either we added it to combinations or we failed and returned
            currcomb.pop()
            trycomb(i + 1, currcomb, currsum)
        trycomb(0, [], 0)
        return combinations
                    
