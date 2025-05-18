team = {
'Jukka': 'software developer', 
'Anne': 'project manager',
'Susanna': 'software developer',
'Aliisa': 'lead developer'
}

while True:
    nimi = input("Anna nimi (quit lopettaa): ")
    if nimi == "quit":
        print("")
        break
    if nimi in team:
        print(f"{nimi} : titteli on {team[nimi]}")
    if nimi not in team:
        rooli = input("Anna rooli: ")
        team[nimi]=rooli
        print("")

for nimi, titteli in team.items():
    print(f"{nimi:10}{titteli}")
