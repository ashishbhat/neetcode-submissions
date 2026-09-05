# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> tuple[bool, int]:
            if not root:
                return (True, 0)
            left_balanced, left = height(root.left)
            right_balanced, right = height(root.right)
            is_balanced = left_balanced and right_balanced and abs(left - right) <= 1
            return (is_balanced, 1 + max(left, right))
        
        return height(root)[0]

            