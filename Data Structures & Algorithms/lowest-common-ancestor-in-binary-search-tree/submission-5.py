# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        # ancestor = {}
        # stack = deque()
        # stack.append(root)
        # while stack:
        #     g = stack.popleft()
        #     ancestor[g] = [g.val]
        #     if g.left:
        #         stack.append(g.left)
        #         ancestor[g].append(g.left.val)
        #     if g.right:
        #         stack.append(g.right)
        #         ancestor[g].append(g.right.val)
        # print(ancestor)

        # for a, c in ancestor.items():
        #     if p.val and q.val in c:
        #         return a
        # return 
