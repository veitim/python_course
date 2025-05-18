def siirra_eteenpain(kellonaika: tuple, tunnit: int, minuutit: int):
    h = kellonaika[0] + tunnit
    m = kellonaika[1] + minuutit
    while h >=24 or m >=60:
        if h >= 24:
            h = h - 24
        if m >= 60:
            h+=1
            m = m - 60
    uusi_aika = (h, m)
    return uusi_aika
    
if __name__ == "__main__":
    kellonaika = (0, 0)
    print(f"Kello on nyt {kellonaika[0]:02d}:{kellonaika[1]:02d}")
    while True:
        tunnit = int(input("Anna lisättävät tunnit: "))
        if tunnit < 0:
            break
        minuutit = int(input("Anna lisättävät minuutit: "))
        aika = siirra_eteenpain(kellonaika, tunnit, minuutit)
        print(f"{aika[0]:02d}:{aika[1]:02d}")
        del kellonaika
        kellonaika = aika
