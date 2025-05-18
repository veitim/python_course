lista = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]

kirjain = input("Anna kirjain: ")
luku = lista.count(kirjain.upper())

print("Kirjain", kirjain.upper(), "löytyy listasta", lista,  luku, "kertaa.")