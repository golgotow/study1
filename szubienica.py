
a = "\nAby kontynować grę, naciśnij klawisz Enter"

def wiadomosc(inputt):
    input(inputt)


invertory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
print("Elementy twojego ekwipunku:")
for item in invertory:
    print(item)

#wyswietlanie długości list
print("twoj dobytek zawiera, ", len(invertory), " elementow")

wiadomosc(a)

# sprawdź, czy element należy do listy, za pomocą operatora in
if "napój uzdrawiający" in invertory:
    print("dożyjesz dnia, w którym stoczysz walkę.")



