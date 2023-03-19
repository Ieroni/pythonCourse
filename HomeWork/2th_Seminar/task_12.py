# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа
print('Task #12')
import random
import math
S = 0
P = 0
i = 0
# while True:
#     if S<P:
#         print(f'Розыгрыш: суммы {S} и произведениея {P}. Циклов было - {i}')
#         break
#     else:
#         S = random.randint(0,2001)
#         P = random.randint(0,1000000)
#         i+=1
S = int(input('введите сумму: '))
P = int(input('введите произведение: '))

# X+Y=S
# X*Y=P --> X=P/Y
# X+P/X=S --> X**2-S*X+P=0
# D= S**2 - 4*P

X = abs((-S+(math.sqrt(S**2-4*P)))/2)
Y = abs((-S-(math.sqrt(S**2-4*P)))/2)
print(X, Y)
# Checking
if X+Y==S:
    t1 = True
if X*Y==P:
    t2 = True
if t1==True & t2==True:
    print('метод верный!')

# for i in range(S):
#     for j in range(P):
#         if S == i + j and P == i * j:
#             print(i, j)