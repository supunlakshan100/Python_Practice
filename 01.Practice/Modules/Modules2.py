# import Modules

# print(Modules.get_name())
# print(__name__)

# print(dir(Modules))

# from os import path

import os.path as path  # alias , it's mean we can use path instead of os.path

import Modules
import sys

if path.exists("Modules.py"):
    print("File exists")
else:
    print("File not exists")


print(sys.argv)
print(sys.path)
print(sys.version)
print(sys.platform)
print(sys.getrecursionlimit())
