from datetime import datetime, timedelta

def main():
    kysy_pvm = input("Anna päiväys muodossa pp.kk.vvvv: ")
    paivia = int(input("Anna lisättävien päivien määrä: "))
    laske_paivays(kysy_pvm, paivia)

def laske_paivays(kysy_pvm, paivia):
    aika = datetime.strptime(kysy_pvm, "%d.%m.%Y")
    lisa_paiva = timedelta(paivia)
    uusi_pva = aika + lisa_paiva
    
    print(f"Uusi päiväys on {uusi_pva.strftime("%d.%m.%Y")}")
    exit()

main()

