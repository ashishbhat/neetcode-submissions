# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0


        def preorder(node: TreeNode, max_path_val: int) -> None:
            nonlocal result
            if node is None:
                return

            if node.val >= max_path_val:
                result += 1

            max_path_val = max(node.val, max_path_val)
            preorder(node.left, max_path_val)
            preorder(node.right, max_path_val)

        preorder(root, root.val)
        return result

            