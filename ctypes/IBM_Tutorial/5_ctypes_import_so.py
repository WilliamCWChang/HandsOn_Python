from ctypes import cdll
# cdll is for Linux share object file
# windll is for Windows DLL file

#__hello.c#########################
#include <stdio.h>
#void hello(){
#    printf("hello\n");
#}
####################################

# $ gcc -shared -fPIC -o some.so hello.c
somelibc = cdll.LoadLibrary("./some.so")
somelibc.hello()


