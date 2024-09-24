print("Введите день: ", end = "")
day = int(input()) #запрашивается день
print("Введите месяц: ", end = "")
month = int(input()) #запрашивается месяц
if month == 12 or month == 1 or month == 2:  #проверка зимних месяцев
    print(f"{day}.{month} - Зима")
elif month < 6: #проверка весенних месяцев
    print(f"{day}.{month} - Весна")
elif month < 9: #проверка летних месяцев
    print(f"{day}.{month} - Лето")    
else: #проверка осенних месяцев
    print(f"{day}.{month} - Осень")