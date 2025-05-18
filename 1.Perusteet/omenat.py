lkm_omena = int(input("Omenoiden lukumäärä? "))
lkm_lapsi = int(input("Lasten lukumäärä? "))

jako = lkm_omena // lkm_lapsi
ylijaama = lkm_omena % lkm_lapsi

print(f"Omenoita per lapsi: {jako}")
print(f"Ylijääviä omenoita: {ylijaama}")
