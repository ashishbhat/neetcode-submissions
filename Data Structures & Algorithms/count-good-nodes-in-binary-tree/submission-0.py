# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def _good_node_helper(self, root: TreeNode, max_val: int = float('-inf')) -> None:
        if root is None:
            return
        if max_val <= root.val:
            self.count += 1

        max_val = max(max_val, root.val)
        self._good_node_helper(root.left, max_val)
        self._good_node_helper(root.right, max_val)



    def goodNodes(self, root: TreeNode) -> int:
        self._good_node_helper(root)
        return self.count
        