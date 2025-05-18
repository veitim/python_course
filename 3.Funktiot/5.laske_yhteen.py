number_first = float(input("Anna ensimmäinen luku: "))
number_second = float(input("Anna toinen luku: "))

def add():
    sum = number_first + number_second + 0.5
    return int(sum)

if __name__ == "__main__":
   print(add())