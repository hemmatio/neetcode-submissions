# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size+= 1
            temp = temp.next
        if size == 1:
            return None
        if size == n:
            return head.next
        idx = size - n
        dummy = ListNode(next=head)
        # remove 0 indexed at size - n, so want to go right before size - n
        while idx > 1:
            head = head.next
            idx -= 1
        head.next = head.next.next
        return dummy.next
        