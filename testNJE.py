#!/usr/bin/python
import os, sys, re, string
import njelib
def main():
    print "Hello, John"
    nje=njelib.NJE("LNX1","LIHT")
    nje.set_debuglevel(1)
    connection=nje.session(host="10.170.30.101",port=175)
    print "Connection LIHT = ", connection
    if not connection:
        print "Connection to LIHT failed"
        return 
    nje.sendMessage("Arf! Arf!")
    nje.disconnect()
    return
main()
