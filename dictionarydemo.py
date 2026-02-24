'''
->key value pair
dict={key:value}
->key must be unique
->no slicing, because no index
->value can be duplicate
methods:
1.get()-only keys are used to get values
2.update()
3.keys()
4.values()
5.items()
'''
dict1={}
print(type(dict1))
dict1={1:"car",2:"bus","bike":3}
print(dict1.get(2))
print(dict1.get("car"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1.update({5:"sruthi"})
print(dict1)
