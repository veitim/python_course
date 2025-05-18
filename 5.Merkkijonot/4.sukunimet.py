lkm = int(input("Anna nimien lukumäärä: "))
lista=[]
i = 0
while True:
    snimi = input("Anna sukunimi: ")
    lista.append(snimi.capitalize())
    i+=1
    if i == lkm:
        break
uusi_lista = list(set(lista))
uusi_lista.sort()
print("")
print(*uusi_lista)