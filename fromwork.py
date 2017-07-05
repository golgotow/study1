import os

def checkFile(paths,myfiles):

    #if os.path.isfile(myfiles):
    if os.path.isfile(paths+myfiles):
        print("file exist")
        cmdls = ("ls -l "+paths+myfiles)
        cmdfile = ("file -s "+paths+myfiles)
        os.system(cmdls)
        os.system(cmdfile)
        os.remove(paths+myfiles)
        print(paths+myfiles+" file removed")
    else:
        print("file not exist")
        print("creating "+paths+myfiles+" ...")
        open(paths+myfiles, 'w').close()
        os.system("ls -l "+paths+myfiles)




print("Podaj pełna scieżke gdzie zrobić plik")
sciezka = input()
print("Podaj nazwe pliku")
nazwa = input()

#myfiles2 = ("/tmp/czesc")
#checkFile("/tmp/czesc",sciezka)
checkFile(sciezka,nazwa)

print("podaj jakas komende")
com = input()
os.system(com)

