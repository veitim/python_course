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

def nayta_tiedot(lista: list)->None:
    summa=0
    aika=0
    for arvo in lista:
       summa+=int(arvo[-2])
       aika+=int(arvo[-1])
       keskiarvo_matka = (summa/ 1000) / len(lista)
       keskiarvo_aika = (aika/ 60) / len(lista)
    print(f"Lainatapahtumia oli {len(lista)} kappaletta.")
    print(f"Pyörillä ajettiin yhteensä {summa/1000:.0f} km")
    print(f"Pyörillä ajettiin keskimäärin {keskiarvo_matka:.1f} km")
    print(f"Ajoaika oli keskimäärin {keskiarvo_aika:.0f} minuuttia")

def main():
    tnimi = input("Anna tiedoston nimi: ")
    try:
        tiedot = lue_tiedot(tnimi)
        if len(tiedot)>0:
            nayta_tiedot(tiedot)
    except:
        print("Tiedostoa ei löytynyt!")

main()