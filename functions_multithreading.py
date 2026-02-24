'''
various functions in multithreading
1.run()
2.start()
3.is_alive()
4.set_name()
5.get_name()
'''
from threading import Thread,current_thread
import time
def display():
    print(current_thread().name)
    time.sleep(5)
    i=10
    while i>0:
        print(i)
        i-=1
def something(n):
    print(current_thread().name)
    for i in range(n):
        print(n*2)
t1=Thread(target=display)
t2=Thread(target=something,args=(10,))
t3=Thread(target=display)
t1.name="sruthi"
t2.name="aishuu"
t3.name="honey"
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()
