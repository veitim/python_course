team = {
'Jukka': 'software developer', 
'Anne': 'project manager',
'Susanna': 'software developer',
'Aliisa': 'lead developer'
}

while True:
    nimi = input("Anna nimi (quit lopettaa): ")
    if nimi == "quit":
        break
    if nimi in team:
        print(f"{nimi} : titteli on {team[nimi]}")
    if nimi not in team:
        print(f"{nimi} : ei kuulu joukkoeeseen")
