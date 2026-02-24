n=int(input("enter ur number:"))
c=0
for i in range(2,n//2):
      if n%i==0:
          c=c+1
if c==0:
    print("prime")
else:
    print("not prime:")
print("using while loop")
i=2
flag=0
while i<n//2:
    if n%i==0:
        flag=flag+1
    i=i+1
if flag==0:
    print("prime")
else:
    print("not prime")



