import multiprocessing
import os
def do_something():
    print("process id",os.getpid())
    print("do something")
def child_process():
    print("process id",os.getpid())
    print("child process")
p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=child_process)
p1.run()
p2.run()
