# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        if not root:
            return res
        q.append(root)

        while q:
            qLen = len(q)
            rightNode = None
            for i in range(qLen):
                rightNode = q.popleft()
                if rightNode and rightNode.left: q.append(rightNode.left)
                if rightNode and rightNode.right: q.append(rightNode.right)
            res.append(rightNode.val)                
        return res