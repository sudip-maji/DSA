from itertools import permutations
from re import A


def printLargest(arr):
    a=[]
    for i in permutations(arr,len(arr)):
        a.append("".join(i))
        # print(a)
    m=max(a)
#     print(m)
#     return "".join(m)
    return m



#     a.append(''.join(arr))
    return 

arr=["26","56","99","29","15","73","27"]

print(printLargest(arr))
    

        


        
        
        