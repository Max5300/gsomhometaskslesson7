from random import randint
x = randint(0, 21)
attempts = 5
print(f"Комьютер загадал число.\nУ вас есть {attempts} попытки(-ок). Удачи!")
for i in range (attempts):
    y = int(input("Попробуйте угадать: "))
    if i == attempts - 1 and y != x:
        print(f"Game over!\nЧисло: {x}")
    else:
        if y > x:
            print("Попробуйте число меньше!")
        elif y < x:
            print("Попробуйте число больше!")
        else:
            print("Победа!")
            break
