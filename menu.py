#!/usr/bin/python3
import sys
from sys import argv
import os
blankvariable = ""
def batt(batt):
    if batt == "battery":
        os.system("/home/cron/battery.sh")
        exit
def show(wysw):
    print("menu.py battery")
    print("rules #network rules")
    exit

def menu(menus):
    if menus == "battery":
        #os.system("/home/cron/battery.sh")
        #exit
        batt(menus)
    elif menus == "rules":
        os.system("ip rule")
        exit
    elif menus == "help":
        print("menu.py battery")
        print("rules")
        exit
    elif menus == "?":
        show(blankvariable)
        exit





print ("Standard Menu for basic Operations in python3 using bash scripts and others")
print ("Version 0.01 alfa, By Sobota Przemysław (17.07..2017)")
if len(sys.argv) > 1:
        print(sys.argv[1])
        a = sys.argv[1]
        menu(a)
else:
        print("no argv, please use help")
        exit
















#!/usr/bin/python3
#import sys
#from sys import argv
#import os
#print ("Standard Menu for basic Operations in python3")
#print ("Version 0.01 alfa, By Sobota Przemysław (17.07..2017)")
#print (argv[1])
#if len(sys.argv) > 1:
#        a = argv[1]
#        print(argv[1])
#else:
#        print("no argv")
#        exit


#print ("argv[0]")

#if a == "":
#        print("nothing paste, existing")
#        exit
