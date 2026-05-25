# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodcount = 0
        def isgood(root, maxsofar):
            nonlocal goodcount
            if not root:
                return
            if root.val >= maxsofar:
                goodcount += 1
                maxsofar = root.val
            isgood(root.left, maxsofar)
            isgood(root.right, maxsofar)
        
        isgood(root, root.val)
        return goodcount

        