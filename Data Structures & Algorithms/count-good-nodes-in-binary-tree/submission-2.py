# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # stack = [(root, root.val)]
        # count = 0
        # while stack:
        #     node, m = stack.pop()
        #     if node.val >= m:
        #         count += 1
        #     m = max(m, node.val)
        #     if node.left:
        #         stack.append((node.left, m))
        #     if node.right:
        #         stack.append((node.right, m))
        # return count

        def dfs(node, m):
            if not node:
                return 0
                
            res = 1 if node.val >= m else 0
            m = max(m, node.val)
            res += dfs(node.left, m)
            res += dfs(node.right, m)
            return res
        
        return dfs(root, root.val)



