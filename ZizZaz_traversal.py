# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#

def zigZagTraversal(root):
    # Write your code here
    result=[]
    f=[]
    q=[]
    if root is None:
        return result
    q.append(root)
    leftright=True
    while len(q)!=0:
        s=[]
        for i in range(len(q)):
            c=q.pop(0)
            s.append(c.data)
            if c.left is not None:
                q.append(c.left)
            if c.right is not None :
                q.append(c.right)
            
        if leftright==True:
            result.append(s)
        if leftright==False:
            l=s[::-1]
            result.append(l)
        
        leftright = not leftright
    abc=[]
    for elements in result:
            for ele in elements:
                abc.append(ele)
    return abc   
#     return result
#     for ele in result:
#         for e in ele:
#             f.append(e)
    
#     return f
   