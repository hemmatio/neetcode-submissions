# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def issame(p, q):
            if (p and not q) or (q and not p):
                return False
            if p and q:
                valsame = p.val == q.val
                leftsame = issame(p.left, q.left)
                rightsame = issame(p.right, q.right)
                return valsame and leftsame and rightsame
            return True

        return issame(p, q)
        