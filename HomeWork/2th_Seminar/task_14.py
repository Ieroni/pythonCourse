# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.
print('Task #14')
import random
n = random.randint(0,1000)
i = 0
listok = list()
print(n)
while 2 ** i <= n:
    listok.append(2 ** i)
    i += 1
print(listok)