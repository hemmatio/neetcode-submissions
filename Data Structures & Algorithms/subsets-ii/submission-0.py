class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort array
        # if already seen this number at this depth, go to the next
        # then call dfs 
        # at each call of dfs, add to the results
        # pop from path, and continue onto the next
        nums.sort()
        result = []
        def dfs(currlist, idx):
            result.append(currlist.copy())

            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    # already used this number at this depth
                    continue
                currlist.append(nums[j])
                dfs(currlist, j + 1)
                currlist.pop()
            
        dfs([], 0)
        return result