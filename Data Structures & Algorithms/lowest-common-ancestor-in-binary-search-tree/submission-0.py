# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue1 = deque()
        queue2 = deque()

        head = root
        while head != None:
            queue1.append(head)
            if p.val == head.val:
                break
            elif p.val > head.val:
                head = head.right
            else:
                head = head.left

        head = root
        while head != None:
            queue2.append(head)
            if q.val == head.val:
                break
            elif q.val > head.val:
                head = head.right
            else:
                head = head.left

        lca = root
        while True:
            if len(queue1) == 0 or len(queue2) == 0:
                break

            l = queue1.popleft()
            r = queue2.popleft()

            if l == r:
                lca = l
            else:
                break
        return lca

        

        