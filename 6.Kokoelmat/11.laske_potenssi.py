def potenssit_2_3(luku):
    duble=(luku ** 2, luku ** 3)
    return duble
if __name__ == "__main__":
    luku = int(input("Anna luku: "))
    duble = potenssit_2_3(luku)
    print(duble[0])
    print(duble[1])