class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        
        def backprop(start, close):
            # invalid: More than n start, more close than start
            if start > n:
                return
            if close > start:
                return
            
            # choices: add a (, add a ).
            path.append('(')
            backprop(start + 1, close)
            path.pop()

            path.append(')')
            backprop(start, close + 1)
            path.pop()

            # goal state
            if start == close == n:
                result.append(''.join(path))


        backprop(0, 0)
        return result