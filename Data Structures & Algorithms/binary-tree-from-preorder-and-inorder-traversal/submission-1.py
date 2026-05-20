# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _buildTreeHelper(self, 
                        preorder: List[int], 
                        inorder: List[int], 
                        in_order_dict: dict[int, int],
                        n: int, 
                        l: int, 
                        r: int) -> Optional[TreeNode]:
        if l == r:
            return n-1,None
        root_val = preorder[n]
        root = TreeNode(root_val)

        root_index = in_order_dict[root_val]
        n,root.left = self._buildTreeHelper(preorder,inorder,in_order_dict, n+1,l, root_index)
        n,root.right = self._buildTreeHelper(preorder,inorder,in_order_dict, n+1,root_index+1, r)
        return n,root



    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_dict = {}
        for i, v in enumerate(inorder):
            in_order_dict[v] = i
        return self._buildTreeHelper(preorder, inorder,in_order_dict, 0, 0, len(preorder) )[1]