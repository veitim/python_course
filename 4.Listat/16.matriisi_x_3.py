def kerro_matriisi_kolmella(matriisi):
    for alkio in range(len(matriisi)):
        for arvo in range(len(matriisi[alkio])):
            matriisi[alkio][arvo] *= 3

if __name__ == "__main__":
    matriisi = [[1, 2, 3, 4, 5, 6],[10, 20, 30]]
    print(matriisi)
    kerro_matriisi_kolmella(matriisi)
    print(matriisi)