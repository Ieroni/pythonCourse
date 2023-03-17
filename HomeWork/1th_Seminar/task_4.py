# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
print('Task #4')

#-M- Method of calcualte of cranes
def CountCranes(s):
    # Let's assume Petya and Seryozha made x number of cranes each.
    # Then Katya made 2x cranes.
    # Total number of cranes is S = 2*(x+x) + x + x = 6x
    # Therefore, x = S/6
    x = int(s//6) #produced by each child
    petyaCranes = seryozhaCranes = int(x)
    if not s%6 == 0:
        difference = s - 6*x
        if difference <=3: 
            katyaCranes = int(difference+4*x) #produced only by Katya while the boys is chilling
            print("Assumed that Katya can make faster then boys, so she created cranes before guy could do enithing")
            return (petyaCranes), (katyaCranes), (seryozhaCranes)
        else: 
            print("the number strictly contradicts the conditions, enter another")
    else:
        katyaCranes = int(4*x)
        return f'Petya made: {(petyaCranes)}, Katya made:  {(katyaCranes)}, Seryozha made: {(seryozhaCranes)}'
        
# enter input data
s = int(input('введите число общего кол-ва журавликов: '))   # Total number of cranes

# ouput data rezult
result = CountCranes(s)
print(result)  






