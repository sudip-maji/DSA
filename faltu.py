class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        n=len(A)
        c=[]
        i=0
        while A or B:
            if not A[i]:
                a=0
            else:
                a=A[i]
            if not B[i]:
                b=0
            else:
                b=B[i]
            
            summ=a+b
            if summ==10:
                c.append(1)
                i+=1
            elif summ>10:
                ans=summ/10
                c.append(ans)
                carry=summ%10
                c.append(carry)
                i+=1
            else:
                c.append(summ)
                i+=1
        return c

