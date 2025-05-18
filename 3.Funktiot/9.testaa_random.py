from random import randint

def arvonta()->int:
    return randint(1,3)

def kasittely()->int:
    lkm=0
    nro=0
    while lkm < 1000000:
        lkm+=1
        arvo=arvonta()
        if arvo==3:
            nro+=1
    return nro
    

def main():
    luku=kasittely()
    print("Satunnaislukugeneraattori arpoi miljoona kertaa luvun väliltä 1-3.")
    print(f"Luvun 3 prosenttiosuus arvotuista luvuista oli vähän yli {luku/1000000*100:.0f}%." )

main()