import base64
import sys

UserName = "YWRtaW4="
Password = "bW94YQ=="




#       # s = '我是字符串'
#       # a = base64.b64encode(s)
#       print(base64.b64decode(UserName))
#       print(base64.b64decode(Password))
#
#       print('Number of arguments:', len(sys.argv), 'arguments.')
code = sys.argv[1]
print(code)
print("\n\n\n\n\n\n")
print(base64.b64decode(code))

