#!/usr/bin/python
import os, sys, re, string
import njelib
def main():
    nje=njelib.NJE("DEV1","LIH1")
    connection=nje.session(host="10.170.30.10",port=175)
    if not connection:
        print "Connection to LIH1 failed"
        return 
    nje.sendmessage("Arf! Arf!")
    return

