# a = [33,32,15,35,33,58,"DJ"]
# b = "d"
# c = "j"
# print(all(a))
# print(bin(b))
# print(ascii(b))
# print(bool(b))
# print(callable(b))
# print(chr(b))
# print(classmethod(b))
# print(complex(b))
# print(delattr(b,c))
# print(bytes(b))
# print(bytearray(b))

import requests

x = requests.get('https://Google.com')

print(x.text)
