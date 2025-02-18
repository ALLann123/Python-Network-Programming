#!/usr/bin/python3
import os
import time

file=input("Enter File To be checked>> ")
st=os.stat(file)

print("file stats: ", file)
mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st

print("-Created: ", time.ctime(ctime))
print("-last accessed:", time.ctime(atime))
print("-last modified:", time.ctime(mtime))
print("-Size:",size,"bytes")
print("-Owner: ",uid, gid)
