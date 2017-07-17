import os

gohome = open("/tmp/testprzemek.txt", 'w')
#gohome.write("#!/usr/bin/env python3\n")
#gohome.write('print("nosz kurwa")\n')
#gohome.write("a = 5\n")
#gohome.write("if a == 5:\n")
#gohome.write("  print ('a jest 5')\n")
#gohome.write("else:\n")
#gohome.write("  print ('a nie jest 5')\n")
gohome.write("#!/usr/bin/env python3\n"
             'print("nosz kurwa")\n'
             "a = 5\n"
             "if a == 5:\n"
             "  print ('a jest 5')\n"
             "else:\n"
             "  print ('a nie jest 5')\n")
gohome.close()
#os.system("chmod +x /tmp/testprzemek.txt")
#os.system("/tmp/testprzemek.txt")
