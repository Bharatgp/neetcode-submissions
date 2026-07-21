# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node,maxInPath):
            if not node : return 
            nonlocal res
            if node.val >= maxInPath:
                res += 1
            maxInPath = max(maxInPath,node.val)
            dfs(node.left,maxInPath)
            dfs(node.right,maxInPath)
        dfs(root,root.val)
        return res            


                                


