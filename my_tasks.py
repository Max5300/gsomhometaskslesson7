def write(name, category, time):
    tasks[name] = {"category": category, "time": time}

tasks = dict()
while True:
    print(f"Простой todo:\n\t1. Добавить задачу.\n\t2. Вывести список задач. \n\t3. Выход")
    try:
        task = int(input("Укажите число: ")) 
        if task == 1:
            name = input("Сформулируйте задачу: ")
            category = input("Добавьте категорию к задаче: ")
            time = input("Добавьте время к задаче: ")
            write(name, category, time)
            continue
        elif task == 2:
            print('\n')
            for i in tasks:
                print(f"Задача: {i}  Категория: {tasks[i]['category']}  Дата: {tasks[i]['time']}")
            print('\n')
        elif task == 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nОшибка ввода. Пожалуйста, попробуйте еще раз.\n\n")
