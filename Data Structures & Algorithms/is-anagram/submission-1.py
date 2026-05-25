from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f1, f2 = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            f1[s[i]] += 1
            f2[t[i]] += 1

        return f1 == f2