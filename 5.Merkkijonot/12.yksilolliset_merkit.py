txt = input("Anna merkkijono: ")
txt1 = txt.upper()
txt2 = set(txt1)
if len(txt1) == len(txt2):
    txt = "Vain yksilöllisiä merkkejä"
else:
    txt = "Ei vain yksilöllisiä merkkejä"
print(txt)