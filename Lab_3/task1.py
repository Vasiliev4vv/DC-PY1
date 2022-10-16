src = not False and True or False and not True

# TODO расписать упрощение выражения
result = True and True or False and True #убираем отрицания
result = True or False # убираем логические "И"
result = True # используем оператор "Или": (1 ИЛИ 0) эквивалентно 1(Истина)
result = True  # TODO подставить результат выражения

print(src == result)
