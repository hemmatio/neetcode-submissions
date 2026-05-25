class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        need_warmer = []
        for i in range(len(temperatures)):
            while len(need_warmer) > 0 and temperatures[i] > temperatures[need_warmer[-1]]:
                idx = need_warmer.pop()
                result[idx] = i - idx
            need_warmer.append(i)
    
        return result