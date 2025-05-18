def lue_tiedot(tnimi: str)->list:
    with open(tnimi, encoding="UTF-8") as tiedosto:
        paluu=[]
        for rivi in tiedosto:
            tiedot=rivi.split(",")
            lista=[]
            for tieto in tiedot:
                lista.append(tieto)
            paluu.append(lista)
    paluu.pop(0)
    return paluu

def nayta_hiljaisin_lahtoasema(lista: list)->None:
    uusi_lista={}
    for rivi in lista:
        asema = rivi[3]
        if asema not in uusi_lista:
            uusi_lista[asema] = 0
        uusi_lista[asema] +=1

    asemat=sorted(uusi_lista.items())
    x = min(uusi_lista.values())
    print("Vähiten lähtöjä oli asemilta:")
    for avain, arvo in asemat:
        if arvo == x:
            print(f"{avain} ({arvo} kappaletta)")
        
def main():
    tnimi = input("Anna tiedoston nimi: ")
    try:
        tiedot = lue_tiedot(tnimi)
        if len(tiedot)>0:
            nayta_hiljaisin_lahtoasema(tiedot)
    except:
        print("Tiedostoa ei löytynyt!")

main()