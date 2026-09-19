# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0


        def preorder(root: TreeNode, max_path_val: int) -> None:
            nonlocal result
            if root is None:
                return

            if root.val >= max_path_val:
                result += 1

            max_path_val = max(root.val, max_path_val)
            preorder(root.left, max_path_val)
            preorder(root.right, max_path_val)

        preorder(root, root.val)
        return result

            