class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
def verticalorder(root,hdist,value):
    if root is None:
        return
    if hdist not in value:
        value[hdist]=root.val

    verticalorder(root.left,hdist-1,value)
    verticalorder(root.right,hdist+1,value)

def getTopView(root):
    # Write your code here.
    vdist=0
    hdist=0
    result=[]
    value={}
    final=[]
    verticalorder(root,hdist,value)
    for x in sorted(value.keys()):
        col=value[x]
        # col=[i[1] for i in sorted(value[x])]
        result.append(col)
#     for elements in result:
#         for ele in elements:
#             final.append(ele)

    return result