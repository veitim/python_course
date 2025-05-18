lista=[]
i = 0
while i < 5:
    syote = int(input("Anna kokonaisluku: "))
    lista.append(syote)
    i+=1
listau = list(set(lista))
listau.sort()
lista.sort()
print(*listau, sep=", ")