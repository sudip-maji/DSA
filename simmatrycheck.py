'''

    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''
def check(left,right):
    if left or right is None:
        return left==right
    if left.data!=right.data:
        return False
    return (check(left.left,right.right) and check(left.right,right.left))
def isSymmetric(root) :
    if root is None:
        return "Asymmetric"
        
    c=check(root.left,root.right)
    if c is True:
        return "Symmetric"
    else:
        return "Asymmetric"
    
    # Write your code here.
    