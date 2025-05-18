i=0
summa=0
arvo = float(input("Anna ensimmäinen numero: "))
while True: 
    if arvo == 0:
        break
    i+=1
    summa+=arvo
    arvo = float(input("Anna seuraava numero: "))
if summa != 0:
    print(f"Keskiarvo on {summa/i:.2f}")
else:
    print("Ei mitään laskettavaa")