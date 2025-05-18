team = {
'Jukka': 'software developer', 
'Anne': 'project manager',
'Susanna': 'software developer',
'Aliisa': 'lead developer'
}
tittelit={}
for arvo, titteli in team.items():
    if titteli not in tittelit:
        tittelit[titteli]=[titteli]
tuloste = sorted(tittelit)
for arvo in tuloste:
    print(arvo)