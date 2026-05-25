class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1. search the rows
        rl = 0
        rr = len(matrix) - 1
        row = -1
        while rl <= rr:
            rmid = ((rr - rl) // 2) + rl
            rval = matrix[rmid][0]
            if rval > target:
                rr = rmid - 1
            elif rval <= target:
                row = rmid
                rl = rmid + 1
        if row == -1:
            return False

        #2. search the cols
        cl = 0
        cr = len(matrix[row]) - 1
        while cl <= cr:
            cmid = ((cr - cl) // 2) + cl
            cval = matrix[row][cmid]
            if cval == target:
                return True
            elif cval > target:
                cr = cmid - 1
            elif cval < target:
                cl = cmid + 1
        return False