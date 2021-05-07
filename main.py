# this is the first version of code
import sys
import os
path = os.path.abspath(os.getcwd())
sys.path.append(path+'\\src')
from firstmod import test1
print("hello4")
print(test1(20))

