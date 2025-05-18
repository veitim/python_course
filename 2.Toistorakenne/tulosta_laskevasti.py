luku = int(input("Anna kokonaisluku: "))
summa = 0
tulostus = "Ei tulostettavaa!"

if luku > 0:
    for i in range(luku, 0, -1):
        print(i, end=" ")
        summa = summa + i
        tulostus = "Lukujen summa on"
    print(f"\n{tulostus} {summa}") # \n = uusi rivi \ = (altGr ja +)
else:
    print(tulostus)