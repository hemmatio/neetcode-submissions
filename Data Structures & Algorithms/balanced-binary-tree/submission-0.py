# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getheight(root):
            if root is None:
                return 0
            left = getheight(root.left)
            right = getheight(root.right)
            return max(left, right) + 1

        def checkheight(root):
            if root is None:
                return True
            leftheight = getheight(root.left)
            rightheight = getheight(root.right)
            if abs(leftheight - rightheight) > 1:
                return False
            return checkheight(root.left) and checkheight(root.right)

        return checkheight(root)
            
        