import os
import sys

os.system("pwd")
os.chdir("/tmp/")
os.system("pwd")
os.chmod("/tmp/kurwa7", 0o444)
os.system("netstat -plnt")
