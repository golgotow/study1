#!/usr/bin/env python3
import sys
from sys import argv
import os
blankvariable = ""
first1 = "ssh root@`docker inspect puppet|" + "grep 192.168.17|grep IPAddress|head -1|" + " awk {'print $2'}|sed " + "'s/"+'"//g' + "'| sed 's/,//g'`"
second1 = "ssh root@`docker inspect salt|" + "grep 192.168.17|grep IPAddress|head -1|" + " awk {'print $2'}|sed " + "'s/"+'"//g' + "'| sed 's/,//g'`"
puppett = str(first1)

def batt(batt):
    if batt == "battery":
        os.system("/home/cron/battery.sh")
        exit

def show(wysw):
    print("")
    print("menu.py battery\n")
    print("rules #network rules\n")
    print("puppet\n")
    print("salt\n")
    print("ssh_server\n")
    print("docker\n")
    print("firewall edit/restart\n")
    print("enter repo Direcotry put menu repo\n")
    print("ilo2\n")
    print("ipmi\n")
    print("jump edit\n")
    print("qnap\n")
    exit

def menu(menus):
    if menus == "battery":
        batt(menus)
    elif menus == "rules":
        os.system("ip rule")
        exit
    elif menus == "puppet":
        os.system(first1)
    elif menus == "salt":
        os.system(second1)
    elif menus == "ssh_server":
        os.system("ssh root@192.168.17.18")
    elif menus == "ilo2":
        os.system("telnet 192.168.13.238")
    elif menus == "ipmi":
        os.system("ipmitool -I lan -H 192.168.1.238 -U root shell")
    elif menus == "jump":
        os.system("ssh jump@jump")
    elif menus == "qnap":
        os.system("ssh admin@qnap")
    elif menus == "repo":
        os.chdir("/backup/repo/pve/ks/")
        os.system("pwd")
        print("wybrano repo")
    elif menus == "docker":
        if len(sys.argv) > 2:
	        os.system("docker "+ sys.argv[2])
        else:
        	print("brak argumentow")
        	exit
    elif menus == "firewall":
        if len(sys.argv) > 2:
            if sys.argv[2] == "edit":
                os.system("vim /root/maskarada")
            elif sys.argv[2] == "restart":
                os.system("/root/maskarada")
        else:
            print("brak argumentow")
    elif menus == "help":
        show(blankvariable)
        exit
    elif menus == "?":
        show(blankvariable)
        exit


print("")
print("Standard Menu for basic Operations in python3 using bash scripts and others")
print("Version 0.15 alfa, By Sobota Przemysław (20.07.2017)")

if len(sys.argv) > 1:
        a = sys.argv[1]
        menu(a)
else:
        print("no argv, please use help")
        exit
