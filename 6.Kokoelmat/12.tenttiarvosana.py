def arvostele_tentti(osallistujat: list, pisteet: int)->tuple:
    lapipaasseet=[]
    for i in osallistujat:
        if i[1] >= pisteet:
            lapipaasseet.append(i)
    return lapipaasseet

def main():
     osallistujat = [("Anne", 30), ("Jukka", 25), ("Aliisa", 40)]
     lapipaasseet = arvostele_tentti(osallistujat, 30)
     print("Tentin läpäisivät")
     for nimi, pisteet in lapipaasseet:
          print(f"{nimi}, {pisteet} pistettä")

if __name__ == "__main__":
     main()