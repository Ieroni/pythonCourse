# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть.
print('Task #10')

import random
while True:
    n = input('введите число монеток: ')
    if n.isdigit():
         n = abs(int(n))
         break
    else:
         print ('Неверно! введите целое цисло')
         

count_Orel = 0
count_Reshka = 0
for _ in range(n): # for _ in range(0,10,2)
    x = random.randint(0,1)
    if x == 0:
        count_Orel += 1
    else:
        count_Reshka += 1
print(f'Розыгрыш: орлов {count_Orel} и решек {count_Reshka} на столе')
if count_Orel < count_Reshka:
    print(f'число орлов надо перевернуть - {count_Orel}')
else:
    print(f'число решек надо перевернуть -  {count_Reshka}')


