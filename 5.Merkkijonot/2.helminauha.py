teksti = input("Anna ensimmäinen teksti: ")
i = 0
while True:
    if txt == "quit":
        break
    txt = teksti.upper()
    if txt == "HELMI":
        i+=1
    teksti = input("Anna seuraava teksti: ")
if i > 0:
    print(f"{i} helmeä")
    print("Näkemiin!")
else:
    print("Näkemiin!")