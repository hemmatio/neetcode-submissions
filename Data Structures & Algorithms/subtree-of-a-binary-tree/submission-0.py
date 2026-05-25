# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isasubtree(root, subroot):
            if (root and not subroot) or (subroot and not root):
                return False
            if not (root or subroot):
                return True
            if not (root.val == subroot.val):
                return False
            return isasubtree(root.left, subroot.left) and isasubtree(root.right, subroot.right)

        def comparetrees(root, subroot):
            if (root and not subroot) or (subroot and not root):
                return False
            isequal = isasubtree(root, subroot) or comparetrees(root.left, subroot) or comparetrees(root.right, subroot)
            if isequal:
                return True
            return False

        return comparetrees(root, subRoot)

        