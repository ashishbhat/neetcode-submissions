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
        lca = root
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
            if not queue1:
                break

            if queue1[0].val == head.val:
                lca = head
                print(f'lca={lca}')
                queue1.popleft()

            if q.val == head.val:
                break
            elif q.val > head.val:
                head = head.right
            else:
                head = head.left

        return lca

        