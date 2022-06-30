from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    prev,temp=None,head
    while temp:
        nxt=temp.next
        temp.next=prev
        prev=temp
        temp=nxt
    return prev    




    
