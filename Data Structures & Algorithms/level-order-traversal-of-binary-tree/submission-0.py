# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        if not root:
            return res
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                if node and node.left : q.append(node.left)
                if node and node.right : q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res        