def kerro_kolmella(lista: list):
    uusi_lista=[]
    for luku in lista:
        luku = luku * 3
        uusi_lista.append(luku)
    return uusi_lista


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6]
    uusi_lista = kerro_kolmella(lista)
    print(lista)
    print(uusi_lista)