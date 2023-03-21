# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
print('Task #18')
import random
n = int(input('ввести натуральное число для кол-ва элементов массива: '))  
print(n)

#-М создание массива
array = []
for _ in range(n): 
    a = random.randint(0,10)
    array.append(a)
print(array)
x = int(input('заданное число для поиска: '))  # Read the number to compare against
    
# Задаем стартовый элемент для поиска
closest_element = array[0]

# метод перебора для поиска ближайшего большего значения (если имеется также ближайшее но меньшее число)
for i in range(1, n):
    if abs(array[i] - x) < abs(closest_element - x):
        closest_element = array[i]

print("ближайшее число в массиве - ", closest_element)  