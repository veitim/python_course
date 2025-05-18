def kerro_kolmella(lista: list):
    for i in range(len(lista)):
        lista[i] *=3

if __name__ == "__main__":
    lista_1 = [1, 2, 3, 4, 5, 6]
    lista_2 = [10, 20, 30]

    print(lista_1)
    kerro_kolmella(lista_1)
    print(lista_1)

    print(lista_2)
    kerro_kolmella(lista_2)
    print(lista_2)