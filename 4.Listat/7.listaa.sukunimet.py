lista = []
while True:
    snimi = input("Anna sukunimi (ok lopettaa): ")
    if snimi == "ok":
        break
    else:
        lista.append(snimi)
lista = list(set(lista))
lista.sort()
print(*lista, sep=", ")
