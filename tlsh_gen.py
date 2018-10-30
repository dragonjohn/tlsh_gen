from __future__ import print_function
from os import listdir
import hashlib
import sys
import tlsh

def compute_1(path):
    with open(path, 'rb') as f:
        data = f.read()
        hs = tlsh.hash(data)
    return hs

def compute_2(path):
    h = tlsh.Tlsh()
    with open(path, 'rb') as f:
        for buf in iter(lambda: f.read(512), b''):
            h.update(buf)
    h.final()
    return h

def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for buf in iter(lambda: f.read(4096), b""):
            hash_md5.update(buf)
    return hash_md5.hexdigest()

#md5 = md5(sys.argv[1])
#print('md5 ', md5)
#hex1 = compute_1(sys.argv[1])
#print('tlsh.hash hex1', hex1)
#hex2 = compute_1(sys.argv[2])
#print('tlsh.hash hex2', hex2)
#print('tlsh.diff(hex1, hex2)', tlsh.diff(hex1, hex2))
#print('tlsh.diff(hex2, hex1)', tlsh.diff(hex2, hex1))
#print('tlsh', tlsh.forcehash(open(sys.argv[1]).read()))

files = listdir(sys.argv[1])
for f in files:
    if str(f).startswith('.'):
        continue
    else:
        filepath = sys.argv[1]+str(f)
        fmd5 = md5(filepath)
        ftlsh = tlsh.forcehash(open(filepath).read())
        print(f, fmd5, ftlsh)

"""
h1 = compute_2(sys.argv[1])
hex1 = h1.hexdigest()
print('tlsh.Tlsh hex1', hex1)
h2 = compute_2(sys.argv[2])
hex2 = h2.hexdigest()
print('tlsh.Tlsh hex2', hex2)
print('h1.diff(h2)', h1.diff(h2))
print('h2.diff(h1)', h2.diff(h1))
print('h1.diff(hex2)', h1.diff(hex2))
print('h2.diff(hex1)', h2.diff(hex1))

h3 = tlsh.Tlsh()
h3.fromTlshStr(hex2)
print('tlsh.Tlsh.fromTlshStr', hex2)
print('h3.diff(h2)', h3.diff(h2))
"""

