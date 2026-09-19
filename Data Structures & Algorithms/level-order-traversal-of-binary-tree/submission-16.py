# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_vals = []

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level_vals.append(node.val)
            if level_vals:
                result.append(level_vals)
        return result