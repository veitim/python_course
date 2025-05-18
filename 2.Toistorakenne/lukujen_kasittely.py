lukuja=0
summa=0
pos_lkm=0
print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    luku=int(input("Luku:"))
    if luku==0:
        break
    elif luku>=0:
        pos_lkm+=1
    lukuja+=1
    summa+=luku
print(f"Lukuja yhteensä {lukuja}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa/lukuja}")
print(f"Positiivisia {pos_lkm}")
print(f"Negatiivisia {lukuja-pos_lkm}")
