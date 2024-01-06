#!/usr/bin/env python3
import subprocess

#get the name of the process
proc_name = input("Process Name: ")

#identify the pid
ps = subprocess.Popen(["ps" ,"aux"], stdout=subprocess.PIPE)
grep1 = subprocess.Popen(["grep",proc_name],stdin=ps.stdout)
print("\n")
pid=input("PID: ")
addr=input("Mem Addr to change: ")
dec_addr = int(addr,16)
cmd = ["dd","if=/home/afk/Desktop/text.txt","bs=1","count=7","seek={}".format(dec_addr),"of=/proc/{}/mem".format(pid),"conv=notrunc"]
subprocess.run(cmd)

#close what you 'OPEN'
