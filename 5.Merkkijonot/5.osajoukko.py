txt1 = input("Anna 1. teksti: ")
txt2 = input("Anna 2. teksti: ")

for kirjain in txt2:
    if txt1.find(kirjain) == -1:
        txt = "Ei ole osajoukko"
        break
    else:
        txt = "Osajoukko"
print(txt)