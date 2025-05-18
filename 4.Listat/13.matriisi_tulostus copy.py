def tulosta(matriisi:list):
    lista = matriisi
    for rivi in lista:
        koko = len(rivi)
        i = 0
        for i in rivi[0:-1:2]:
            print(i, end=" ")
            print(* rivi, sep="")
            merkki = "|"
            kerroin = 2
            arvo = kerroin * merkki
            rivi[i] = arvo
            i+=1
            
if __name__ == "__main__":
    matriisi=[[4,2,1,3,1,2,5,2,1,2,1,2,4,2,1,3,1],
    [1,2,1,3,1,1,1,5,1,4,1,2,1,2,1,2,1,2,2,2,1],
    [4,4,1,6,1,4,4,2,1,2,1,2,1,1,1,1,1],
    [1,7,1,6,1,4,1,2,1,2,1,2,1,2,1,2,2],
    [1,7,1,6,1,4,1,2,1,2,4,2,1,3,1]]
    tulosta(matriisi)
    matriisi=[[0,3,1,3,1,3,1,3,1,3,1],
    [0,3,1,2,1,1,1,2,1,3,1,2,1,1,1],
    [0,3,1,1,1,3,1,1,1,3,1,1,1,3,1],
    [1,2,1,1,5,2,1,1,1,2,5],
    [0,1,2,2,1,3,1,3,1,3,1,3,1]]
    tulosta(matriisi)
