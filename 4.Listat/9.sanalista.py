from urllib.request import urlopen
sanalista = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read().splitlines()
lista=[]
for sana in sanalista:
    sana = sana.decode("utf-8")
    if len(sana) == 15:
        lista.append(sana)
print(*lista, sep=", ")