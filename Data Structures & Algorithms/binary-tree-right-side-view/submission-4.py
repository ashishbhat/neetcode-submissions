# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        current_level = []
        next_level = [root]

        if not root:
            return right_view

        while next_level:
            current_level.clear()
            for node in next_level:
                current_level.append(node)
            right_view.append(current_level[-1].val)

            next_level.clear()
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return right_view
            
            