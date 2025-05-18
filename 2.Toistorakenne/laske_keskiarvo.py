i=1
summa = 0
text = "Anna ensimmäinen numero: "
while True: 
    arvo = float(input(text))
    i+=1
    text = "Anna seuraava numero: "

    if arvo == 0:
        break
    if arvo > 0 and arvo < 0:
        summa = arvo + arvo
print("Keskiarvo on", summa)

#keskiarvo = arvo / i