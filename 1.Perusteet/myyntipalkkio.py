hinta = int(input("Anna auton myyntihinta: "))

if hinta >= 50000:
    palkkio = hinta*0.015
    print(f"Myyntipalkkio on {palkkio:.2f} €.")

if hinta < 50000:
    palkkio = hinta*0.01
    if palkkio > 200:
        print(f"Myyntipalkkio on {palkkio:.2f} €.")
    else:
        print(f"Myyntipalkkio on 200 €.")
