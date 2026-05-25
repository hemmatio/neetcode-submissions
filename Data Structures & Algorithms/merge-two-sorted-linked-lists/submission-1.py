# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        sol = head
        while list1 and list2:
            if list1.val < list2.val:
                sol.next = ListNode(list1.val)
                list1 = list1.next
            else:
                sol.next = ListNode(list2.val)
                list2 = list2.next
            sol = sol.next
        if list1:
            sol.next = list1
        else:
            
            sol.next = list2
            
        return head.next
        