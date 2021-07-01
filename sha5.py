import timeit
from time import time
import sys

num = 100
string="abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"

setup_c="""
import hashlib
string="abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
"""


import hashlib;
import sys;

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

print(sys.version)
with open('/proc/cpuinfo') as f:
	for line in f:
	    if line.startswith('model name'):
		print('CPU:', line.split(':')[1].strip())
		break
print ("Word: ",string)

print("\nMethod:\t\t\tSeconds")

t=timeit.timeit(stmt="hashlib.sha1(string.encode()).hexdigest()", setup=setup_c, number=num)
print("SHA-1:\t\t\t",t)
t=timeit.timeit(stmt="hashlib.sha256(string.encode()).hexdigest()", setup=setup_c,  number=num)
print("SHA-256:\t\t",t)
t=timeit.timeit(stmt="hashlib.sha512(string.encode()).hexdigest()", setup=setup_c,  number=num)
print("SHA-512:\t\t",t)


print("\nHashes")
print("SHA-1\t",hashlib.sha1(string.encode()).hexdigest())
print("SHA-256\t",hashlib.sha256(string.encode()).hexdigest())
print("SHA-512\t",hashlib.sha512(string.encode()).hexdigest())

