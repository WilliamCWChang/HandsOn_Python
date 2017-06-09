from ctypes import * 
print("=========================")
print("C variable")
print("=========================")
print('\n\n')


p = create_string_buffer(10)
p.raw
print(">>p.raw = {0}\n".format(repr(p.raw)))

p.value = b"Student"
print("p.value = b\"Student\"")
p.raw
print(">>p.raw = {0}\n".format(repr(p.raw)))

p.value = b"Big"
print("p.value = b\"Big\"")
p.raw
print(">>p.raw = {0}\n".format(repr(p.raw)))
