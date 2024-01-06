#!/usr/bin/env python3

import sys
#check for errors in input
pid = input("Enter PID of Process: ") 
readText = input("Enter existing Text: ")
writeText = input("Enter new Text: ")

#error end script
def error():
    sys.exit(1)

#find the range of heap from maps
mapsfile = open("/proc/{}/maps".format(pid), "r") #could fail !!

#parsing maps(.txt) for heap info
for line in mapsfile:
    currline = line.split()
    if "[heap]" in currline:
        break
    else:
        continue

offset, permission = currline[0], currline[1]

#check permissions
if permission[0] == 'r':
    print("[*] File is '{}' Readable".format(permission[0]))
else:
    print("[*] ERROR: File is '{}' NOT Readable".format(permission[0]))
    error()
if permission[1] == 'w':
    print("[*] File is '{}' Writeable".format(permission[1]))
else:
    print("[*] ERROR: File is '{}' NOT Readable".format(permission[1]))
    error()

#note start-end points of heap
addrs = offset.split("-")
addr_start = int(addrs[0], 16)
addr_end = int(addrs[1], 16)

#open mem file in read-write binary
mem_file = open("/proc/{}/mem".format(pid),'rb+') #check of failiure

#move pointer to heap start
mem_file.seek(addr_start)

#convert heap to list of bytes by reading it in one chunk of size(heap)
heap = mem_file.read(addr_end-addr_start) #list of 'bytes' from mem for easy search

#find the string in heap and note index
i = heap.index(bytes(readText,"ASCII")) #check for error!

#move pointer to string location
mem_file.seek(addr_start + i)
#convert writeText to bytes and write to memory
mem_file.write(bytes(writeText,"ASCII")) 

print("[*] Memory Write Successful!")

#close files
mapsfile.close()
mem_file.close()

