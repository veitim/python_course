def main():
    lista=[]
    i = 0
    while i < 5:
        syote = int(input("Anna kokonaisluku: "))
        lista.append(syote)
        i+=1
    lista_kasittely(lista)

def lista_kasittely(lista):
    luku = len(lista)
    suurin = max(lista)
    pienin = min(lista)
    summa = sum(lista)
    return print(f"Count: {luku} \n min: {pienin} \n max: {suurin} \n sum: {summa}")

main()