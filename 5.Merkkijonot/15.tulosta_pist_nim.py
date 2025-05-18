def tulosta_lista(lista:list) -> list:
    for tieto in lista:
        nimi = tieto[0].capitalize()
        print(f"{nimi:20}-{tieto[1]:>5}")

if __name__ == "__main__":
    tulosta_lista([['kristiina',100], ['matti', 70], ['aliisa', 150]])