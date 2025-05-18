from datetime import date
from calendar import monthrange

def print_month_calendar(vv, kk):
    months=["Tammi","Helmi","Maalis","Huhti","Touko","Kesä",
            "Heinä","Elo","Syys","Loka","Marras","Joulu"]
    my_date = date(vv, kk, 1)
    day_of_week = monthrange(my_date.year, my_date.month)[0] # indeksissä 0 on kuukauden 1. päivän viikonpäivä 0-6 ma-su
    days_in_month = monthrange(my_date.year, my_date.month)[1]  # indeksissä 1 on päivien lukumäärä kuukaudessa 
    i = kk-1
    print(f"\n > {months[i]} {my_date.year} <")
    print(" Ma Ti Ke To Pe La Su")
    pva=0
    day=1
    vaihto=1
   
    while day <= days_in_month:
        if day_of_week > pva:
            print(end="   ")
            pva+=1
            vaihto+=1
        elif vaihto == 7 or day == days_in_month:
            print(end=f"{day:3d}\n")
            day+=1
            vaihto=1 
        else:
            print(end=f"{day:3d}")
            day+=1
            vaihto+=1

def main():
    vv = int(input("Anna vuosi: "))
    kk = int(input("Anna kuukausi: "))
    print_month_calendar(vv, kk)


main()