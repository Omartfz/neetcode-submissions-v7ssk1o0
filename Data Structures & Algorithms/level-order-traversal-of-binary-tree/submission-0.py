# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=collections.deque()
        res=[]
        q.append(root)
        while q:
            qLen=len(q)
            col=[]
            for _ in range (qLen):
                node=q.popleft()
                if node:
                    col.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if col:
                res.append(col)
        return res



            
        