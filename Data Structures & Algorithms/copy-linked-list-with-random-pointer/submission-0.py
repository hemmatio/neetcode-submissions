"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        headdummy = head
        new = Node(0)
        newdummy = new
        while head:
            new.next = Node(head.val)
            mapping[head] = new.next
            head = head.next
            new = new.next
        head = headdummy
        new = newdummy.next
        while head:
            new.random = mapping.get(head.random)
            head = head.next
            new = new.next
        return newdummy.next

        
