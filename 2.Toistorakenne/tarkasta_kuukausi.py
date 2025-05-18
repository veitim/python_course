while True:
    kk = input("Anna kuukauden numero: ")
    try:
        if int(kk) >= 1 and int(kk) <=12:
            break
        else:
            print(f"{kk} ei ole kelvollinen kuukausinumero")
    except:
        print(f"'{kk}' ei ole kelvollinen kuukausinumero")

print("OK")