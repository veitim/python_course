lkm_kaynti = int(input("Anna käyntikertojen vuosimäärä: "))
hinta_pva = float(input("Anna päivälipun hinta: "))
hinta_vuosi = float(input("Anna vuosilipun hinta: "))

tulo = lkm_kaynti * hinta_pva

if tulo > hinta_vuosi:
    print(f"Vuosilippu tulee {tulo - hinta_vuosi:.2f} euroa halvemmaksi")
if tulo == hinta_vuosi:
    print(f"Vuosilippu ja päiväliput tulevat samanhintaisiksi")
if tulo < hinta_vuosi:
    print(f"Päivälippu tulee {hinta_vuosi - tulo:.2f} euroa halvemmaksi")