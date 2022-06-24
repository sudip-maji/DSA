# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if root is None:
                return 0
            return fun(root.left)+fun(root.right)+1
        return fun(root)
            