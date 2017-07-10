# program najlepszy wynik


scores = []

choice = None

while choice != "0":

    print(
        """
        Najlepsze Wyniki
        
        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        3 - usuń wynik
        4 - posortuj wyniki
        """
    )
    choice = input("Wybierasz: ")
    print()
    #Zakończ program
    if choice == "0":
	    print("Do widzenia!")
    #Wypisz tabelę najlepszych wyników
    elif choice == "1":
        print("Najlepszego wyniki")
        for score in scores:
        	print(score)
#Dodaj wynik
    elif choice == "2":
        score = int(input("Jaki wynik uzyskałeś?: "))
        scores.append(score)
#usuń wynik
    elif choice == "3":
        score = int(input("Który wynik usunąć ? "))
        if score in scores:
            scores.remove(score)
        else:
            print("nie ma na liście wyników")
# posortuj wyniki

    elif choice == "4":
        scores.sort(reverse=True)
        print(scores)
# nieznana opcja
    else:
        print("opcja nie jest znana.")


