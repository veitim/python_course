try:
	hinta = float(input("Anna hinta: "))
	print(f"Arvonlisäverollinen hinta on {hinta*1.24:.2f}")
except:
	print("Virheellinen hinta!")