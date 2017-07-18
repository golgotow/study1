#!/usr/bin/env python3
import sys
from sys import argv
import os
blankvariable = ""
first1 = "ssh root@`docker inspect puppet|" + "grep 192.168.17|grep IPAddress|head -1|" + " awk {'print $2'}|sed " + "'s/"+'"//g' + "'| sed 's/,//g'`"
#first = "ssh root@`docker inspect puppet|"
#second = "grep 192.168.17|head -1| "
#third = " awk {'print $2'}|sed "
#four = "'s/"+'"//g'
#five = "'| sed 's/,//g'`"
#puppett = str(first+second+third+four+five)
puppett = str(first1)

def batt(batt):
    if batt == "battery":
        os.system("/home/cron/battery.sh")
        exit

def show(wysw):
    print("menu.py battery")
    print("rules #network rules")
    print("puppet")
    print("docker")
    exit

def menu(menus):
    if menus == "battery":
        batt(menus)
    elif menus == "rules":
        os.system("ip rule")
        exit
    elif menus == "puppet":
        os.system(first1)
    #elif menus == "docker":
    #    os.system("docker "+ sys.argv[2])
    #    exit
    elif menus == "docker":
        if len(sys.argv) > 2:
	        os.system("docker "+ sys.argv[2])
        else:
        	print("brak argumentow")
        	exit
    elif menus == "help":
        show(blankvariable)
        exit
    elif menus == "?":
        show(blankvariable)
        exit



print ("Standard Menu for basic Operations in python3 using bash scripts and others")
print ("Version 0.01 alfa, By Sobota Przemysław (17.07.2017)")

if len(sys.argv) > 1:
        a = sys.argv[1]
        menu(a)
else:
        print("no argv, please use help")
        exit




