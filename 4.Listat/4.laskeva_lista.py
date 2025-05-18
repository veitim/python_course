lista=[]
i = 0

while i < 5:
    syote = int(input("Anna kokonaisluku: "))
    lista.append(syote)
    i+=1
lista.sort(reverse = True)
print("")
print(*lista, sep=" ")