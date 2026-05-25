class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # see if the counts of s1 are ever in s2
        counts_s1 = [0] * 26
        for i in range(len(s1)):
            counts_s1[ord(s1[i]) - ord('a')] += 1
        counts_s2 = [0] * 26
        sp = 0
        for i in range(len(s2)):
            # always update the count.
            # if condition violated, move sp forward until its not.
            idx = ord(s2[i]) - ord('a')
            counts_s2[idx] += 1
            while counts_s2[idx] > counts_s1[idx]:
                spidx = ord(s2[sp]) - ord('a')
                if counts_s2[spidx] > 0:
                    counts_s2[spidx] -= 1
                sp += 1
            if i - sp + 1 == len(s1) and counts_s1 == counts_s2:
                return True

                    
        return False
            
            