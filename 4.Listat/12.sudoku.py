sudoku = [
[9, 0, 0, 0, 8, 0, 3, 0, 0],
[2, 0, 0, 2, 5, 0, 7, 0, 0],
[0, 2, 0, 3, 0, 0, 0, 0, 4],
[2, 9, 4, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 7, 3, 0, 5, 6, 0],
[7, 0, 5, 0, 6, 0, 4, 0, 0],
[0, 0, 7, 8, 0, 3, 9, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 2]
]
def rivi_oikein(sudoku: list, rivi_nro: int)->bool:
    rivi = sudoku[rivi_nro]
    lista=[]
    for arvo in rivi:
        if arvo > 0 in rivi:
            lista.append(arvo)
    if len(set(lista))<len(lista):
        return "False"
    else:
        return "True"
print(rivi_oikein(sudoku, 0))
print(rivi_oikein(sudoku, 1))