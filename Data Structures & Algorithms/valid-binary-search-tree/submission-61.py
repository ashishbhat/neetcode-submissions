# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN_VAL = -1000000000
        MAX_VAL = 1000000000

        def preorder(root, minn, maxx):
            if root is None:
                return True
            # print(f'root.val={root.val}, minn={minn}, maxx={maxx}')
            # print(maxx <= root.val <= minn)
            if maxx <= root.val or root.val <= minn:
                return False
            elif root.left and root.left.val >= root.val:
                return False
            elif root.right and root.right.val <= root.val:
                return False
            else:
                return preorder(root.left, minn , root.val) and preorder(root.right, root.val, maxx)

        return preorder(root, MIN_VAL, MAX_VAL)
