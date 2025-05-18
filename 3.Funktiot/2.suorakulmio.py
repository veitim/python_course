korkeus = int(input("Anna suorakulmion korkeus: "))
leveys = int(input("Anna suorakulmion leveys: "))    

def print_rectangle():
    merkki="*"
    x = merkki*leveys
    i=0
    while i<korkeus:
        i+=1
        print(x)

print_rectangle()