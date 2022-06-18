# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalorder(root,vdist,hdist,value):
        if root is None:
            return
        if hdist not in value:
            value[hdist]=[(vdist,root.val)]
        else:
            value[hdist].append((vdist,root.val))
        verticalorder(root.left,vdist+1,hdist-1,value)
        verticalorder(root.right,vdist+1,hdist+1,value)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vdist=0
        hdist=0
        result=[]
        value={}
        
        verticalorder(root,vdist,hdist,value)
        for x in sorted(value.keys()):
            col=[i[1] for i in sorted(value[x])]
            result.append(col)
        return result
    
        