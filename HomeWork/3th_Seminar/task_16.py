#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
print('Task #16')

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = int(input("Enter the number to be counted: "))

count = 0
for num in arr:
    if num == x:
        count += 1

print("The number", x, "occurs", count, "times in the array.")

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = int(input("Enter the number to be counted: "))

count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

if x in count_dict:
    print("The number", x, "occurs", count_dict[x], "times in the array.")
else:
    print("The number", x, "does not occur in the array.")