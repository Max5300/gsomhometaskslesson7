summ = 0
while True:
    try:
        x = input("Введите число или Стоп для выхода: ")
        if x.lower() == "стоп":
            print(f"Сумма: {summ}")
            break
        summ += int(x)
    except ValueError:
        print("Ошибка ввода.")
        continue

        
        
