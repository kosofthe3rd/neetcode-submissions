# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cur = root
        q = deque([root])
        res = []
        res.append(root.val)
        while q:
            temp = []
            for _ in range(len(q)):
                p = q.popleft()
                if p.left:
                    q.append(p.left)
                    temp.append(p.left.val)
                if p.right:
                    q.append(p.right)
                    temp.append(p.right.val)
            if temp:
                res.append(temp[-1])
        
        return res