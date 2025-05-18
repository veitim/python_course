def toiseksi_suurin(lista: list):
      poisto = set(lista)
      kopio = sorted(poisto)
      kopio.reverse()
      return kopio[1]
      
def main():
      print(toiseksi_suurin([1, 5, 4, 5, 4, 3]))
main()