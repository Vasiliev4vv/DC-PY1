import random


def get_unique_list_numbers() -> list[int]:
    num = 15  # 15 - число необходимых чисел
    list_ = [random.randint(-10, 10) for x in range(num)]  # создаём 15 случайных чисел
    list_unique = set(list_)  # удаляем повторяющиеся значения
    while len(list_unique) < num:  # дополняем уникальные числа, чтобы было 15 уникальных случайных чисел
        list_ = list_ + [random.randint(-10, 10) for x in range(num - len(list_unique))]
        list_unique = set(list_)
    list_ = [numb for numb in list_unique]  # по условию нужно вернуть список.
    return list_  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
