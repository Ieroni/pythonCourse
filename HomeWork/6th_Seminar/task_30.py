# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print('Task #30')
# Get user input for first element, difference, and number of elements
a1 = int(input("Enter the first element: "))
d = int(input("Enter the difference: "))
n = int(input("Enter the number of elements: "))

# Create an empty array to store the arithmetic progression
arithmetic_progression = []

# Fill the array with elements of the arithmetic progression using the formula
for i in range(1, n+1):
    arithmetic_progression.append(a1 + (i-1) * d)

# Print the array
print(arithmetic_progression)
