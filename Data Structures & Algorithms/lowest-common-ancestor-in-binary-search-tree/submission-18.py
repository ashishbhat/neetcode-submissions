# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        print(f'root = {root.val} left = {left.val if left else None} right = {right.val if right else None}')
        if (left is not None and (left.val is p.val or left.val is q.val)) and (right is not None and (right.val is p.val or right.val is q.val)):
            return root
        elif left is not None:
            if root.val is p.val or root.val is q.val:
                return root
            return left
        elif right is not None:
            if root.val is p.val or root.val is q.val:
                return root
            return right
        elif root.val is p.val or root.val is q.val:
            return root
        else:
            return None