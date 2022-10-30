def delete(list_, index=None):
    if index == None: # TODO реализовать функцию удаления элемента из списка по индексу
        index = -1
    if index == -1:
        list_changed = list_[:index]
    else:
        left_list = list_[:index]
        right_list = list_[index+1:]
        list_changed = left_list + right_list
    return list_changed
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3] - в этом комментарии, похоже, ошибка!
