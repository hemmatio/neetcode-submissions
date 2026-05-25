class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. arrange into one array: [(p, s)] then sort by p decreasing
        # 2. add top p to stack
        # 3. compute time to finish: (target - pos) / speed
        # 4. iterate by the pos: if time is less than time of what's in stack, keep whats in the stack
        # 4b. else, add it to stack
        # 5. return length of stack

        # If a car reaches the target before one thats ahead of it, it means that it will be bottlenecked by the one thats in front of it.

        def finishtime(pos, speed, target):
            return (target - pos) / speed
        
        pos_speed = [(position[i], speed[i]) for i in range(len(position))]
        print(f"pos speed is {pos_speed}")
        pos_speed.sort(reverse=True)
        print(f"pos speed is {pos_speed}")

        stack = []
        for i in range(len(pos_speed)):
            if len(stack) == 0:
                stack.append(pos_speed[i])
                continue
            leadertime = finishtime(stack[-1][0], stack[-1][1], target)
            currtime = finishtime(pos_speed[i][0], pos_speed[i][1], target)
            if currtime <= leadertime:
                continue # leader will hold back this car, so don't add it
            stack.append(pos_speed[i]) # this car won't intersect with any leaders
        return len(stack)
        

        