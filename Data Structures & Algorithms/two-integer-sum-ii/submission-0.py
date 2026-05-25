class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                idx2 = numbers.index(target - numbers[i])
                if idx2 != i:
                    return [min(i, idx2) + 1, max(i, idx2) + 1]
                
        return None