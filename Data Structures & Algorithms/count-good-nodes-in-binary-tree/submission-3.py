# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def _good_node_helper(self, root: TreeNode, max_val: int = float('-inf')) -> int:
        if root is None:
            return 0

        max_val = max(max_val, root.val)
        left_count = self._good_node_helper(root.left, max_val)
        right_count = self._good_node_helper(root.right, max_val)

        total_count = left_count + right_count
        if max_val <= root.val:
            total_count += 1
        return total_count

    def goodNodes(self, root: TreeNode) -> int:
        return self._good_node_helper(root)
        