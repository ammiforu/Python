import datetime
print("Hello World today is my first day in python ")
print("Date : Feb 13 2024 CST")
Pday = datetime.date(2024,  2,  13)
print(Pday)
Tday = datetime.date.today()
print(Tday)

diff = Tday-Pday
print(f'Days Past from starting :{diff.days} days')
