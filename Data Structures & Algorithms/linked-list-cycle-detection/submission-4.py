# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastpointer = head
        while head:
            head = head.next
            for _ in range(2):
                if fastpointer:
                    fastpointer = fastpointer.next
                else:   
                    return False
            if head == fastpointer:
                return True
        return False
            
            

        