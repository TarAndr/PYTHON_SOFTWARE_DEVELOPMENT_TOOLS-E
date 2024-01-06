import random
import operator

# Создаем словарь и заполняем его случайными элементами
my_dict = {i: random.randint(1, 100) for i in range(10)}

# Выводим исходный словарь
print("Исходный словарь:")
print(my_dict)

# Сортируем словарь по значениям
sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))

# Выводим отсортированный словарь
print("\nОтсортированный словарь по значениям:")
print(sorted_dict)
