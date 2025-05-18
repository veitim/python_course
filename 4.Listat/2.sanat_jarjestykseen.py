lista=[]
while True:
    vastaus=input("Anna sana (x lopettaa): ")
    if vastaus == "x":
        break
    else:
        lista.append(vastaus)
        lista.sort()
for i in range(len(lista)):
  print(lista[i])