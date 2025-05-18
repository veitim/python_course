def tulosta(matriisi:list):
    lista = matriisi
    for rivi in lista:
        koko = len(rivi)
        i = 0
        while i < koko:
            kerroin = rivi[i]
            if i == 0 or i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12 or i == 14 or i == 16 or i == 18 or i == 20: 
                merkki = '|'
                arvo = kerroin * merkki
                rivi[i] = arvo
                #print(arvo, end="")
            else:
                merkki = "PA"
                arvo = kerroin * merkki
                rivi[i] = arvo
                #print(arvo, end="")
            i+=1
        print(*rivi, sep="")
    print("")
        
        
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
    