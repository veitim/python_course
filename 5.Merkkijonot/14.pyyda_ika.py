def pyyda_ika():
    while True:
        ika = input("Anna ikä: ")
        if ika.isdigit():
            if int(ika) > 0 and int(ika) <= 100:
                txt = f"Antamasi ikä on {ika}"
                break
            else:
                print("Antamasi arvo ei ole kelvollinen!")
        else:
            print("Antamasi arvo ei ole kelvollinen!") 
    return txt

if __name__ == "__main__":
    txt = pyyda_ika()
    print(txt)