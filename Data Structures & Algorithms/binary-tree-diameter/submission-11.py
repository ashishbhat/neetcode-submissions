# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(root: TreeNode) -> int:
            nonlocal res
            left = 1 + depth(root.left) if root.left else 0
            right = 1 + depth(root.right) if root.right else 0
            res = max(res, left + right)
            return max(left, right)
        
        depth(root)
        return res

        
        
