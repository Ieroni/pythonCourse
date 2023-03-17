# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
print('Task #8')

# -M- method for caclculate of number of chokolate slices


def can_break_chocolate_bar(n, m, k):
    # If the total number of slices is less than k, it is not possible to break off k slices
    if n * m < k:
        return False

    # If k is divisible by n or m, it is always possible to break off k slices
    if k % n == 0 or k % m == 0:
        return True

    # Calculate the possible break points using integer division and modulo operators
    x = k // n
    y = k // m
    if k % n == 0 and x <= m:
        return True
    if k % m == 0 and y <= n:
        return True

    # If no break point is found, it is not possible to break off k slices
    return False


# enter input data
n = int(input('введите число длины шоколадки: '))   # Total number of row
m = int(input('введите число ширины шоколадки: '))   # Total number of column
# number of desired slices
k = int(input('введите требуемое число долек после разлома: '))

# ouput data rezult
result = can_break_chocolate_bar(n, m, k)
print(result)
