# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

 

        # if left is p and right is q or  right is p and left is q
        if left and right and (
            (left.val == p.val and right.val == q.val) or (left.val == q.val and right.val == p.val)
        ):
            return root


        # if root is p or q
        if root.val == p.val or root.val == q.val:
            return root
        if left:
            return left
        if right:
            return right

        # else None
        return None


