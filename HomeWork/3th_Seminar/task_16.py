#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
print('Task #16')
import random
mySet = set()

n = int(input("Введите число N элементов в массиве: "))
array = []
#-М создание массива
for _ in range(n): # for _ in range(0,10,2)
    a = random.randint(0,10)
    array.append(a)
print(array)

x = int(input("введите число для поска числа Х: "))

count = 0
for num in array:
    if num == x:
        count += 1

print("число", x, "встречается", count, "раз в массиве.")

mySet =(n, array, x)
print(mySet)