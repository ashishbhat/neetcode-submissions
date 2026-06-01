# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter: int = 0

        def find_diameter(root) -> int:
            nonlocal diameter
            if not root:
                return 0

            left_diameter = find_diameter(root.left)
            right_diameter = find_diameter(root.right)
            subtree_diameter = left_diameter + right_diameter
            diameter = max(diameter, subtree_diameter)
            return 1 + max(left_diameter, right_diameter)

        find_diameter(root)
        return diameter