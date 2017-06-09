import sys
from ctypes import * 
print("=========================")
print("C call DLL")
print("=========================")
print('\n\n')

somelibc = cdll.LoadLibrary("./libmodbus.so") 
