from ctypes import * 
print("=========================")
print("Easy use")
print("=========================")
print('\n\n')


i = c_int(45) 
print("i = c_int(45)")
print(">>i.value = {0}".format(i.value))

i.value = 56
print("i.value = 56")
print(">>i.value = {0}".format(i.value))