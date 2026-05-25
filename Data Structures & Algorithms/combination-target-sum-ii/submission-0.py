class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def dfs(i, currcomb, currsum):
            if currsum == target:
                combs.append(currcomb.copy())
                return
            if i >= len(candidates):
                return
            if currsum + candidates[i] > target:
                return
        
            # loop until non-duplicate found
            j = i
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + currsum > target:
                    break # all further are bigger
                currcomb.append(candidates[j])
                dfs(j + 1, currcomb, currsum + candidates[j])
                currcomb.pop()

        dfs(0, [], 0)
        return combs
