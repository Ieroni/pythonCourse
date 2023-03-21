# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
print('Task #18')
n = int(input('ввести натуральное число для кол-ва элементов массива: '))  # Read the number of elements in the array
print(n)
a = list(map(int, input().split()))  # Read the array elements
print(a)
x = int(input('заданное число для поиска: '))  # Read the number to compare against

# Initialize the closest element to the first element of the array
closest_element = a[0]

# Iterate through the rest of the array elements and update the closest element if a closer one is found
for i in range(1, n):
    if abs(a[i] - x) < abs(closest_element - x):
        closest_element = a[i]

print(closest_element)  # Print the closest element