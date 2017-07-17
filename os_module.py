import os

gohome = open("/tmp/testprzemek.txt", 'w')
gohome.write("#!/bin/bash\n")
gohome.write("df -h")
gohome.write("czesc\n"
             "jeden\n"
             "dwa\n"
             "trzy\n"
             "cztery\n"
             "piec\n")
gohome.close()
#os.system("chmod +x /tmp/testprzemek.txt")
#os.system("/tmp/testprzemek.txt")
