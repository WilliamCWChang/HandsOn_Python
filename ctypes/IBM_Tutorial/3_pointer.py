from ctypes import * 
print("=========================")
print("C Pointer")
print("=========================")
print('\n\n')

i = c_int(999) 
pi = pointer(i)
print(">>pi.contents = {0}\n".format(repr(pi.contents)))

pi.contents = c_long(1000)
print(">>pi.contents = {0}\n".format(repr(pi.contents)))