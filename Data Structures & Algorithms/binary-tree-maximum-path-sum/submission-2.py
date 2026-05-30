# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum: int = float("-inf")

        def max_path(root: Optional[TreeNode]) -> int:
            nonlocal max_path_sum
            if root is None:
                return 0
            if root.left is None and root.right is None:
                max_path_sum = max(max_path_sum, root.val)
                return root.val
            left = max_path(root.left)
            right = max_path(root.right)
            max_path_sum = max(max_path_sum, 
                            max(root.val, root.val + left, root.val + right, root.val + left + right))
            return max(root.val, root.val + left, root.val + right)
        return max(max_path(root),
                max_path_sum)