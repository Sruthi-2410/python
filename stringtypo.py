str1="Hi Hello 123"
x=len(str1)
l=0
d=0
u=0
for i in range(x):
    if(str1[i].islower()):
        l=l+1
    elif(str1[i].isupper()):
        u=u+1
    elif(str1[i].isdigit()):
        d=d+1
    else:
        print("null")
print(l," ",u," ",d)
str3="123"
print(str1.endswith(str3))
print(str1.split(" "))
