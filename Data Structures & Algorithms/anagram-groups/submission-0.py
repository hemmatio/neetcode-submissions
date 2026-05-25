from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            frequency = [0] * 26
            for character in word:
                frequency[ord(character) - ord('a')] += 1
            groups[tuple(frequency)].append(word)
        return list(groups.values())
        
        
