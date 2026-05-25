# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global pathlength
        pathlength = 0
        # length is left tree height + right tree height
        def height(root):
            global pathlength
            lh, rh = 0, 0
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)

            pathlength = max(pathlength, (lh + rh))
            return max(lh, rh) + 1


        height(root)
        return pathlength
        