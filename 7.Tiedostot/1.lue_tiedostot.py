hae = input("Anna tiedoston nimi: ")
txt = "Python 3.10 keywords"
print(txt)
print("-"*len(txt))
try:
    with open(hae, encoding="UTF-8") as tiedosto:
        sisalto = tiedosto.read()
        print(sisalto)
except:
    print(f"Tiedostoa {hae} ei löytynyt")