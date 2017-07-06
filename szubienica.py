
a = "\nAby kontynować grę, naciśnij klawisz Enter"

def wiadomosc(inputt):
    input(inputt)


invertory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
print("Elementy twojego ekwipunku:")
for item in invertory:
    print(item)

#wyswietlanie długości list
print("\ntwoj dobytek zawiera, ", len(invertory), " elementow")

wiadomosc(a)

# sprawdź, czy element należy do listy, za pomocą operatora in
if "napój uzdrawiający" in invertory:
    print("\ndożyjesz dnia, w którym stoczysz walkę, bo masz napój uzdrawiający")



#wyświetl jeden element wskazany przez indeks
index = int(input("\n Podaj indeks elementu inwentarza:"))
print("\nPod indeksem", index, "znajduje się", invertory[index])

#wyświetl wycinek indeksu

start =int(input("\n Podaj poczatek wycinka "))
finish = int(input("\n Podaj koniec wycinka "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(invertory[start:finish])

wiadomosc(a)

# dokonaj konkatenacji dwój list

chest = ["złoto", "klejnoty"]
print("ZNajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego zawiera:")
invertory += chest
print("Twoj aktualny inwentarz to:")
print(invertory)

wiadomosc(a)

#przypisz poprzez indeks


print("Wymieniasz swój miecz na kuszę.")
invertory[0] = "kusza"
print("Twój aktualny inwentarz to:\n")
print(invertory)

wiadomosc(a)

#przypisz poprzez wycinek
print("Zużywasz swoje złoto i klejnoty na zakup kuli do wróżenia.")
invertory[4:6] = ["kula do wróżenia"]
print("Twój aktualny inwnetarz to:")
print(invertory)

wiadomosc(a)

#usuń element z listy

print("W bitwie tracisz część ekwipunku\n")
print("Tracisz", invertory[2])
del invertory[2]
print("Twój aktualny stan sprzętu to: ")
print(invertory)



wiadomosc(a)

# usuń wycinek

print("Twoje", invertory[:2], "zostały skradzione")
del invertory[:2]
print("Twój aktualny ekwipunek to ")
print(invertory)


wiadomosc(a)



