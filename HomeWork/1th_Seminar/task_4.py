# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
print('Task #4')

#-M- Method of calcualte of cranes
def count_cranes(s):
    # Let's assume Petya and Seryozha made x number of cranes each.
    # Then Katya made 2x cranes.
    # Total number of cranes is S = 2*(x+x) + x + x = 6x
    # Therefore, x = S/6
    if not s%6 == 0:
        print("Error of entering: someone  of kids is cheating :)")
        return None
    else:
        x = round(s/6, 0)
    
    # Calculate the number of cranes made by each child
    petya_cranes = seryozha_cranes = x
    katya_cranes = 4*x
    
    # Return the number of cranes made by each child as a tuple
    return int(petya_cranes), int(katya_cranes), int(seryozha_cranes)

# enter input data
s = int(input('введите число общего кол-ва журавликов: '))   # Total number of cranes

# ouput data rezult
result = count_cranes(s)
print(result)  






