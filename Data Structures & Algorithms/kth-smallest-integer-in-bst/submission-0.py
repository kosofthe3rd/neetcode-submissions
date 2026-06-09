# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        minheap = []

        heapq.heapify(minheap)
        values = [root.val]
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                values.append(node.left.val)
            if node.right:
                stack.append(node.right)
                values.append(node.right.val)
        
        heapq.heapify(values)
        print(values)
        val = 0
        while k > 0:
            val = heapq.heappop(values)
            k -=1
        return val
        

            
            



        