s = """В разные эпохи и у разных народов число Пи имело разное значение. Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело значение 3.162 китайцы пользовались числом, равным 3.1459 Буквенное обозначение число Пи получило только в 1706 году – оно происходит от начальных букв двух греческих слов, означающих окружность и периметр. Буквой π число наделил математик Джонс, а прочно вошла в математику она уже в 1737 году."""
curnum = 0
q = 0
maxx = 0
summ = 0
lst = s.split()
nums = []
for i in lst:
    try:
        curnum = float(i)
        q += 1
        summ += curnum
        nums.append(str(curnum))
        if maxx < curnum:
            maxx = curnum
    except ValueError:
        continue
print(f"Встречающиеся в тексте числа: {' '.join(nums)}")
print(f"Количество числе в тексте: {q}")
print(f"Сумма чисел в тексте: {summ}")
print(f"Максимальное число в тексте: {maxx}")
