from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verticalorder(root,hdist,value):
    if root is None:
        return
    if hdist not in value:
        value[hdist]=root.data
    else:
        value[hdist]=root.data
    verticalorder(root.left,hdist-1,value)
    verticalorder(root.right,hdist+1,value)	
def bottomView(root):
    vdist=0
    hdist=0
    result=[]
    value={}
    verticalorder(root,hdist,value)
    for x in sorted(value.keys()):
         col=value[x]
        # col=[i[1] for i in sorted(value[x])]
         result.append(col)
#     for elements in result:
#         for ele in elements:
#             final.append(ele)

    return result
    
    # Write your code here.
    # This function returns a list of nodes which is the required bottom view of the tree.
    


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1
