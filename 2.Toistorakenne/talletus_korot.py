korkoprosentti = float(input("Anna korkoprosentti: "))
veroprosentti = float(input("Anna pääomatuloveroprosentti: "))
paaoma = float(input("Anna talletuksen suuruus: "))
vuosi = int(input("Anna vuosien lukumäärä: "))
alku_vuosi = 1

korko = korkoprosentti/100 * paaoma
vero = veroprosentti/100 * korko
paaoma = paaoma + korko - vero

while True:
    print(f"Vuosi {alku_vuosi}: {paaoma:.2f}")
    alku_vuosi += 1
    korko = korkoprosentti/100 * paaoma
    vero = veroprosentti/100 * korko
    paaoma = paaoma + korko - vero
    if vuosi < alku_vuosi:
        break