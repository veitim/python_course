luku = input("Anna kokonaisluku: ")

try:
    int(luku)
    print("OK")
except:
    print(f"'{luku}' ei ole kokonaisluku")