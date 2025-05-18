def laske_kirjaimet(merkkijono: str, merkki: str) -> int:
    i = 0
    merkkijono = merkkijono.upper()
    merkki = merkki.upper()
    for kirjain in merkkijono:
        if kirjain == merkki:
            i+=1
    return i

if __name__ == "__main__":
    merkkijono = input("Anna merkkijono: ")
    merkki = input("Anna merkki: ")
    arvo = laske_kirjaimet(merkkijono, merkki)
    print(arvo)