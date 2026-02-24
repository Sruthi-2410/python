r=int(input("enter no of rows "))
c=int(input("enter no of columns "))
arr=[]
for i in range(r):
    a=[]
    for j in range(c):
        ele=int(input(f"enter {i+1}, {j+1} element "))
        a.append(ele)
    arr.append(a)
for r in arr:
    print(r)