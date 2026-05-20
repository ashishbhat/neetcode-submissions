# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(root: Optional[TreeNode]) -> int:
            nonlocal diameter
            if root == None:
                return 0

            depth_left = depth(root.left)
            depth_right = depth(root.right)

            diameter = max(diameter, (depth_left + depth_right))
            return 1 + max(depth_left, depth_right)
        depth(root)
        return diameter
        