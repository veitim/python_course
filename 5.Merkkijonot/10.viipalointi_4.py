txt = input("Anna merkkijono: ")
i=1
handle = []
while i<=len(txt):
    handle.append(txt[-i])
    i+=1
txt_new = "".join(handle)
if txt.upper() == txt_new.upper():
    print("Kyllä")
else:
    print("Ei")