# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        queue = deque()
        queue.append((root, root.val))

        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                good_nodes += 1
            if node.left:
                queue.append((node.left, max(node.left.val, max_val)))
            if node.right:
                queue.append((node.right, max(node.right.val, max_val)))
        return good_nodes