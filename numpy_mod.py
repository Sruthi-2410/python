import numpy as np
n=int(input("enter no of elements "))
arr=np.array([])
for i in range(n):
    ele=int(input(f"enter the {i+1} element "))
    arr=np.append(arr,ele)
print(arr)