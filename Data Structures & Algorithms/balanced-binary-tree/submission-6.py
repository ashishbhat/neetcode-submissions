# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l = self._depth(root.left)
        r = self._depth(root.right)
        if l == -1 or r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        #print(f'root={root.val} l_height={l},r_height={r}')
        # print(f'root={root.val} height={max(l,r)}')

        return 1 + max(l,r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self._depth(root) == -1:
            return False
        else:
            return True

