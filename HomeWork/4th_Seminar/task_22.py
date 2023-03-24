# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
print('Task #22')
import string
import random

# string.ascii_letters 
n = int(input('введите число для набора n: '))
m = int(input('введите число для нарбора m: '))
setDigits1 = set(' '.join([random.choice(string.digits) for _ in range(n)]))
setDigits2 = set(' '.join([random.choice(string.digits) for _ in range(m)]))
print(setDigits1)
print(setDigits2)

for i in setDigits2:
    coincidences = setDigits1 & setDigits2
    kool = list(coincidences)
    kool.sort()
for i in kool:
    print(i, end=' ')
