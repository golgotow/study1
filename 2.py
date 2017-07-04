import os


myfile = ("/tmp/czesc")

if os.path.isfile(myfile):
    print("file exist")
    os.system("ls -l /tmp/czesc")
    os.system("rm -f /tmp/czesc")
    print("file removed")
else:
    ##os.system("touch /tmp/czesc")
    open("/tmp/czesc", 'w').close()
    print("file not exist")
    print("creating...")
    os.system("ls -l /tmp/czesc")


