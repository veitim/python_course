naiset = int(input("Anna naisopiskelijoiden määrä: "))
miehet = int(input("Anna miesopiskelijouden määrä: "))

summa = naiset + miehet
if summa==0:
    print(f"Naisia: {0:.1f} %")
    print(f"Miehiä: {0:.1f} %")
else:
    print(f"Naisia: {(naiset/summa)*100:.1f} %")
    print(f"Miehiä: {(miehet/summa)*100:.1f} %")