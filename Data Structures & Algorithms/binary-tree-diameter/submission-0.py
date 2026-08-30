# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Carries the best diameter
        res = 0

        def dfs(node):
            nonlocal res

            # 1. Base Case:
            if not node: return 0

            # Get the heights of the left and right subtrees of the current node
            L = dfs(node.left)
            R = dfs(node.right)

            # Update the diameter -> it is sum of the two heights of the nodes's subtrees
            res = max(res, L + R)

            return 1 + max(L, R) # The height

        dfs(root)

        return res 