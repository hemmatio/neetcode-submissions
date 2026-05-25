class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        startpointer = 0
        maxseq = 1
        currseq = 1
        frequencies = [0] * 26
        frequencies[ord(s[0]) - ord('A')] = 1
        maxfreq = 1
        for i in range(1, len(s)):
            currseq += 1
            frequencies[ord(s[i]) - ord('A')] += 1
            maxfreq = max(frequencies)

            #invalid: k + maxfreq < currseq
            while k + maxfreq < currseq:
                currseq -= 1
                frequencies[ord(s[startpointer]) - ord('A')] -= 1
                startpointer += 1
                maxfreq = max(frequencies)
            
            maxseq = max(currseq, maxseq)


        return maxseq