# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        carryover = 0
        dummy = l1
        while l1 and l2:
            thisval = carryover + l1.val + l2.val
            carryover = 0
            if thisval > 9:
                carryover = 1
                thisval -= 10
            l1.val = thisval
            prev = l1
            l1 = l1.next
            l2 = l2.next
        while l1:
            thisval = carryover + l1.val
            carryover = 0
            if thisval > 9:
                carryover = 1
                thisval = thisval - 10
            l1.val = thisval
            prev = l1
            l1 = l1.next
            
        while l2:
            thisval = carryover + l2.val
            carryover = 0
            if thisval > 9:
                carryover = 1
                thisval = thisval - 10
            prev.next = ListNode()
            prev.next.val = thisval
            l1 = prev.next
            prev = l1
            l1 = l1.next
            l2 = l2.next

        if carryover:
            prev.next = ListNode(carryover)

        return dummy