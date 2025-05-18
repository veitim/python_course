merkkijono1 = input("Anna 1. merkkijono: ")
merkkijono2 = input("Anna 2. merkkijono: ")

txt1 = merkkijono1.replace(" ", "")
txt2 = merkkijono2.replace(" ", "")

if len(txt1) == len(txt2):
    for kirjain in txt2:
        if txt1.find(kirjain) == -1:
            txt = "Eri merkit"
            break
        else:
            txt = "Samat merkit"
else:
    txt = "Eri merkit"

print(txt)