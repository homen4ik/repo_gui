years_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
month = int(input('Введите месяц года числом: '))
if month > 0 and month < 13:
    print(years_list[month-1])
else:
    print('Нет такого месяца')

years_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
m = int(input('Введите месяц года числом: '))
if m in years_dict:
    print(years_dict[m])
else:
    print('Нет такого месяца')


