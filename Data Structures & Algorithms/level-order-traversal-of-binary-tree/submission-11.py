# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_level = [root]
        result = []

        while current_level:
            temp = []
            next_level = []

            for node in current_level:
                temp.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not  None:
                    next_level.append(node.right)

            result.append(temp)
            current_level.clear()
            current_level = next_level
        return result


