# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow is the midpoint.
        midpoint = slow.next
        slow.next = None # list is split in half
        prev = None
        while midpoint:
            temp = midpoint.next
            midpoint.next = prev
            prev = midpoint
            midpoint = temp
        # now prev is the head of the (reversed) 2nd half

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
