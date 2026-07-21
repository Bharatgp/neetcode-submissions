# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True
        if (p and not q)  or (q and not p): return False

        c1 = p.val == q.val
        c2 = self.isSameTree(p.left,q.left)
        c3 = self.isSameTree(p.right,q.right)

        if(c1 and c2 and c3): return True

        return False

