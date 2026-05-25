class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # list is sorted. That means that if last item plus first item is more than target, the last item is not usable.
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            thesum = numbers[p1] + numbers[p2]
            if thesum == target:
                return [p1 + 1, p2 + 1]
            if thesum > target:
                p2 -= 1
                continue
            p1 += 1