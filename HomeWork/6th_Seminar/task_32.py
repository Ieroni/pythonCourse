# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

print('Task #32')
# Get user input for the list of numbers, minimum value, and maximum value
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(x) for x in numbers]  # convert input strings to integers
minimum = int(input("Enter the minimum value: "))
maximum = int(input("Enter the maximum value: "))

# Initialize an empty list to store the indices of the numbers in the range
indices = []

# Loop through the list of numbers and check if each number is in the range
for i in range(len(numbers)):
    if minimum <= numbers[i] <= maximum:
        indices.append(i)

# Print the indices of the numbers in the range
print("Indices of numbers in range:", indices)
