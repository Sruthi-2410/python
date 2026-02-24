'''
relative module
->subprocess module:
import subprocess
->multi processing module:
import multiprocessinng
cmd="dir"
subprocess.Popen(cmd,shell=True)
cmd1="python --version"
print(subprocess.call(["python","--version"]))
'''
import subprocess
cmd1="python --version"
#prog="java sample"
subprocess.call(["java","sample"])
