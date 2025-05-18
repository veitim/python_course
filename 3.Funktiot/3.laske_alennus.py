def compute_discount():
    newprice = price * (discount/100)
    return newprice

if __name__ == "__main__":
   price = float(input("Anna hinta: "))
   discount = float(input("Anna alennusprosentti: "))
   print(f"Alennus on {compute_discount():.2f} euroa")
    