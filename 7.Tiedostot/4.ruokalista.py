import json

def lue_tiedot(tnimi: str)->list:
    with open(tnimi, encoding="UTF-8") as tiedosto:
        data = tiedosto.read()
    tiedot = json.loads(data)
    return tiedot

def nayta_tiedot(lista: list)->None:
    ruokalista=[]
    menus_for_days=lista["MenusForDays"]
    for tiedot in menus_for_days:
        ruokatiedot = tiedot["SetMenus"]
        for annokset in ruokatiedot:
            annos=annokset["Components"]
            if len(annos) > 0:   
                for arvo in annos:
                    ruoka = arvo.split("(")
                    ruokalista.append(ruoka[0].strip())
    ruokalista.sort()
    print(", ".join(ruokalista))
    
def main():
    tnimi = input("Anna tiedoston nimi: ")
    try:
        tiedot = lue_tiedot(tnimi)
        if len(tiedot)>0:
            nayta_tiedot(tiedot)
    except:
        print("Tiedostoa ei löytynyt!")
main()