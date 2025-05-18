lista=[]
luku = int(input("Kuinka monta kokonaislukua syötät? "))
i = 0

while i < luku:
    syote = int(input("Anna kokonaisluku: "))
    lista.append(syote)
    i+=1
lista.reverse()
print("")
print(*lista, sep=" ")