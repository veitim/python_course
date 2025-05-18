koko = int(input("Anna pyramidin korkeus: "))

def print_pyramid():
    i=1
    tulostus=("**")
    if koko == 0:
        return
    while i<koko:
        print(" "*(-1+i)+tulostus*(koko-i)+"*")
        i+=1
    print(" " * (koko - 1) + "*")

if __name__ == "__main__":
    print_pyramid()