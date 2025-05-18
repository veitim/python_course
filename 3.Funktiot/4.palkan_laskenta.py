hour_salary = float(input("Anna tuntipalkka: "))
hour_work = int(input("Anna tehdyt tunnit: "))

def compute_earnings():
    if hour_work > 40:
        overtime = hour_work - 40
        salary = (hour_salary*40) + (overtime*(hour_salary*1.5))
    else:
        salary = hour_salary * hour_work
    return salary

if __name__ == "__main__":
   print(f"Ansiosi ovat {compute_earnings():.2f} euroa")