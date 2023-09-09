# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

arr = [randint(-20,20) for i in range(20)]
print(arr)
min_value = int(input("Введите минимум: "))
max_value = int(input("Введите максимум: "))

def find_indices(arr, min_value, max_value):
    indices = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indices.append(i)
    return indices

result = find_indices(arr, min_value, max_value)
print(result)