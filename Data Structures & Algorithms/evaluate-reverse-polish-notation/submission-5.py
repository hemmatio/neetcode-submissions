from math import trunc
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        numbers = deque()
        for i in range(len(tokens)):
            if tokens[i] in operations:
                rightnum = numbers.pop()
                leftnum = numbers.pop()
                numbers.append(eval(f"trunc({leftnum} {tokens[i]} {rightnum})"))
                continue
            else:
                numbers.append(tokens[i])
        return int(numbers.pop())

            
