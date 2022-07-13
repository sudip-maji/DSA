from collections import defaultdict


m={}
res=defaultdict(list)
res[2].append("abs")
res[(4,5)].append("def")
res[2].append("hjk")
print(res.values())
print(res)