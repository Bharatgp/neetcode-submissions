# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        
        def dfs(node,val):
            if not node: return -101
            nonlocal res
            if node.val>=val:
                res=res+1
            val=max(node.val,val)
            dfs(node.left,val)
            dfs(node.right,val)    
        dfs(root,root.val)
        return res