# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _kthSmallest_helper(self, 
    root: Optional[TreeNode], 
    k: int, count: 
    int = 0) -> tuple[int, Optional[int]]:
        if root is None:
            return (count, None)
        count, val = self._kthSmallest_helper(root.left, k, count)
        if val is not None:
            return (count, val)
        count += 1
        if count == k:
            return (count, root.val)
        count, val = self._kthSmallest_helper(root.right, k, count)
        if val is not None:
            return (count, val)
        return (count, None)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self._kthSmallest_helper(root,k)[1]

