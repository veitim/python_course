team = {
'Jukka': 'software developer', 
'Anne': 'project manager',
'Susanna': 'software developer',
'Aliisa': 'lead develope'
}

maet = {}
meat = sorted(team)
for avain, arvo in team.items():
    print(avain, end=" ")
print("")
print(* meat)
while team:
    avain, arvo = team.popitem()
    maet[avain] = arvo
    print(avain, end=" ")