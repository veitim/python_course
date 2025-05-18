def lisaa_jasen(team: dict):
    kysy = input("\tAnna nimi: ")
    nimi = kysy.capitalize()
    rooli = input("\tAnna rooli: ")
    if len(nimi) < 2 or len(rooli) < 2:
        print("\tNimi ja/tai rooli liian lyhyt!")
    else:
        team[nimi]=rooli

def poista_jasen(team: dict):
    printti = sorted(team)
    for arvo in printti:
        print(f"\t{arvo}")
    kysy = input("\tAnna poistettavan jäsenen nimi: ")
    poista = kysy.capitalize()
    if poista in team:
        print(f"\t{poista} poistettiin")
        del team[poista]
    else:
        print(f"\tNimeä {poista} ei löydy!")
        return
    
def nayta_jasenet(team: dict):
    for nimi, arvo in team.items():
        print(f"\t{nimi:10}{arvo}")
    
def main():
    team = {
    'Jukka': 'software developer', 
    'Anne': 'project manager',
    'Susanna': 'software developer',
    'Aliisa': 'lead developer'
    }
    while True:
        valinta = int(input("1. lisää jäsen\n2. poista jäsen\n3. näytä jäsenet\n0. lopeta\nAnna valintasi: "))
        if valinta == 0:
            break
        elif valinta == 1:
            print("")
            lisaa_jasen(team)
            print("")
        elif valinta == 2:
            print("")
            poista_jasen(team)
            print("")
        elif valinta == 3:
            print("")
            nayta_jasenet(team)
            print("")
        else:
            print("")
            print("Väärä valinta")
            print("")
            
main()
