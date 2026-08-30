# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 

        # Base case is 1 (only the root node)
        # Recursion to get the depths of the left subtree and the right subtree
        L = self.maxDepth(root.left) # L = depth of left subtree
        R = self.maxDepth(root.right) # R = depth of right subtree

        # Note: this is postorder

        return 1 + max(L, R)
        