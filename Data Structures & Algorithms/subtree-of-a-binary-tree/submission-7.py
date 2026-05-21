# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 is node2 is None:
                return True

            if (node1 is None) != (node2 is None):
                return False

            if node1.val != node2.val:
                return False

            return same(node1.left, node2.left) and same(node1.right, node2.right)
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False

            