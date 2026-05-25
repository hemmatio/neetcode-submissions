class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(leftidx, rightidx):
            height = min(heights[leftidx], heights[rightidx])
            length = rightidx - leftidx
            return height * length

        p1 = 0
        p2 = len(heights) - 1
        max_area = 0
        while p1 < p2:
            curr_area = getArea(p1, p2)
            max_area = max(curr_area, max_area)
            if heights[p1] < heights[p2]:
                p1 += 1
                continue
            else:
                p2 -= 1
        return max_area

