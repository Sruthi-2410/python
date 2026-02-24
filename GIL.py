'''
GIL-global interpreter lock
1. subprocess
2. mutilprocessing
used for serial execution of threads
-> when t1 is excuting t2,t3 are locked
-> when t2 is executing t3,t1 are locked
'''
from threading import Thread,current_thread
import time
def something(n):
    print(current_thread().name)
    while n>0:
        n-=1
def do_something(n):
    print(current_thread().name)
    while n>0:
        n-=1        
n=10_000_000        
st=time.time()
t1=Thread(target=something,args=(n,))
t2=Thread(target=do_something,args=(n,))
t1.start()
t2.start()
print("total time= ",time.time()-st)

