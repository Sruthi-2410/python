
'''print(s.count(10))
-> it has no index
methods:
1.add()
2.update()
3.remove()
4.pop()
operatos:
1.union()
2.intersection()
3.difference()
4.issubset()
5.issuperset()
'''
'''set1={1,2,3}
print(type(set1)
set1.add(10)
set1.add(20)
set1.update([60])
set1.pop()
set1.remove(10)
print(set1)'''
set1={10,20,30,40,50}
set2={40,50}
print(set1.union(set2))
print(set1.intersection(set2))
set3=set1.difference(set2)
print(set3)
print(set2-set1)
print(set2.issubset(set1))
print(set1.issuperset(set2))



