teksti = input("Anna teksti: ")
summa = 0
for luku in teksti:
    if luku.isdigit():
        summa+=int(luku)
print(f"\n Lukujen summa on {summa}")