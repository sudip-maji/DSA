data=[[5,7,10],[67,89],[1,4,6,9],[67,90,68]]
def avg(data):
   a=sum(data)/len(data)
   print(a)
   return a
print(sorted(data,key=avg))
# for elements in data:
#    a=sum(elements)/len(elements)
#    print(a)
