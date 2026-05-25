from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_ls = 0
        curr_ls = 0
        frequencies = defaultdict(int)
        for i in range(len(s)):
            frequencies[s[i]] += 1
            while frequencies[s[i]] > 1:
                frequencies[s[start]] -= 1
                curr_ls -= 1
                start += 1

            curr_ls += 1
            if max_ls <= curr_ls:
                max_ls = curr_ls

        return max_ls
