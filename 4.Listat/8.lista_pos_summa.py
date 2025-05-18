def main():
    lista=[]
    i = 0
    while i < 5:
        syote = int(input("Anna kokonaisluku: "))
        lista.append(syote)
        i+=1
    vastaus = positive_sum(lista)
    print(vastaus)
    

def positive_sum(lista):
    lista_uusi = [x for x in lista if x > 0]
    summa = sum(lista_uusi)
    if len(lista_uusi) > 0:
        return summa
    else:
        return 0

main()