# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sol = None
        while list1 and list2:
            if list1.val < list2.val:
                if sol is None:
                    sol = ListNode(list1.val)
                    head = ListNode(0, sol)
                else:
                    sol.next = ListNode(list1.val)
                    sol = sol.next
                list1 = list1.next
            else:
                if sol is None:
                    sol = ListNode(list2.val)
                    head = ListNode(0, sol)
                else:
                    sol.next = ListNode(list2.val)
                    sol = sol.next
                list2 = list2.next
        if list1:
            if sol:
                sol.next = list1
            else:
                return list1
        else:
            if sol:
                sol.next = list2
            else:
                return list2
            
        return head.next
        