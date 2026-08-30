# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, best):
            # Base case -> empty subtree contributes 0 good nodes
            if not node: return 0

            # Identify if this is a good node or not
            if node.val >= best:
                good = 1
            else:
                good = 0

            # preorder portion --> Get the largest val, store in best, this travels down
            best = max(best, node.val)

            # Get the number of good nodes 
            goodL_nodes = dfs(node.left, best)
            goodR_nodes = dfs(node.right, best)

            # postorder portion --> the number of good nodes travels up
            return good + goodL_nodes + goodR_nodes # The number of good nodes

        best = float("-inf")
        return dfs(root, best)