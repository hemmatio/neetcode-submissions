from collections import defaultdict
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combs = []
        numslen = len(nums)
        def dfs(i, currcomb, frequencies):
            if i == numslen:
                combs.append(currcomb.copy())
                return
            
            
            for j in range(numslen):
                if frequencies[nums[j]] == 0:
                    currcomb.append(nums[j])
                    frequencies[nums[j]] += 1
                    dfs(i + 1, currcomb, frequencies)
                    currcomb.pop()
                    frequencies[nums[j]] = 0          
                
        dfs(0, [], defaultdict(int))
        return combs

        