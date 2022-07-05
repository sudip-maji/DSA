# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self,root,level,q):  
        if root is None:
            return
        if len(q)==level:
            q.append(root.val)
        self.fun(root.right,level+1)
        self.fun(root.left,level+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        self.fun(root,0,q)
        return q
        