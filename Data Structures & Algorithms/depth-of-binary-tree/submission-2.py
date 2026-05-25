# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def getdepth(root, depth):
            if root:
                prevdepth = depth
                if root.left and root.right:
                    depth = max(getdepth(root.left, prevdepth + 1), getdepth(root.right, prevdepth + 1))
                elif root.left:
                    depth = getdepth(root.left, prevdepth + 1)
                elif root.right:
                    depth = getdepth(root.right, prevdepth + 1)
            return depth
        if root:
            return getdepth(root, 1)
        return 0
        