from datetime import datetime, timedelta

def main():
    try:
        pvm_alku = input("Anna alkupäivä muodossa pp.kk.vvvv: ")
        aika_alku = datetime.strptime(pvm_alku, "%d.%m.%Y")
        pvm_loppu = input("Anna loppupäivä muodossa pp.kk.vvvv: ")
        aika_loppu = datetime.strptime(pvm_loppu, "%d.%m.%Y")
    except:
        print("Antamasi arvo ei ole kelvollinen")
        exit()    
    erotus = laske_paivat(aika_alku, aika_loppu)
    print("Päivien", pvm_alku, "ja",
           pvm_loppu, "välissä on", erotus, "päivää.")

def laske_paivat(aika_alku, aika_loppu):
    paivia = aika_loppu - aika_alku
    return paivia.days

main()