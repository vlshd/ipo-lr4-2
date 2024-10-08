def chisla(numbers): # создание функции
    return [x**2 for x in numbers] # квадраты чисел
l_list = [1, 2, 3, 4, 5] # создание списка
list = chisla(l_list) # возвращение нового списка
print(list)  # Вывод