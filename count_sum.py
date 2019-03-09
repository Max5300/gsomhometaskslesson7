try:
    summ = 0
    number = tuple(input("Введите число: "))
    for i in number:
        if int(i) % 2 == 1:
            summ += pow(int(i), 2)
    print(f"Сумма квадратов нечетных цифр в числе: {summ}")
except ValueError:
    print("Ошибка ввода. Переданная строка не является числом")
