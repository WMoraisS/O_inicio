def is_year_leap(year):
    if year % 4 == 0 :
        if year % 100 == 0 and year % 400 != 0: return False
        else: return True
    else: return False

def days_in_month(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    bissexto = is_year_leap(year)

    if month == 2:
        if bissexto == True: x = 29
        else: x = 28
        return x
    else:
        return months[month-1]
    
def day_of_year(year, month, day):
    days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if day <= days_of_months[month-1]:
        for i in range(month-1):
            day += days_in_month(year, month + 1)
        return day

print(day_of_year(2000, 2, 28))
