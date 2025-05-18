try:
    paiva = int(input("Anna viikonpäivän numero "))
    if paiva >= 1 and paiva <= 7:
        print("OK")
    else:
        print("Syötä kokonaisluku väliltä 1 ja 7")
except:
        print("Syötä kokonaisluku väliltä 1 ja 7")
