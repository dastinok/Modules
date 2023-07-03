from sys import argv

__all__ = ['_leap_year', 'my_date']

def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True



def my_date(date: str):
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year < 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 31:
            return True
        else:
            return _leap_year(year) and day <= 29

if __name__ == '__main__':
    if len(argv) == 2:
        _, date = argv
        print(my_date(date))
    else:
        print("Дата для проверки не указана!")