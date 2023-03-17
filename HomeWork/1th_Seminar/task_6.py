# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
import random
print('Task #6')

# -M- Method of generate a six-digit random number


def is_lucky(ticket_number):
    # Convert the ticket number to a string
    ticket_str = str(ticket_number)

    # Check if the ticket number has six digits
    if len(ticket_str) != 6:
        return False
    # Get the sum of the first three digits and the last three digits
    first_half_sum = int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2]) #could used - sum(map(int, ticket_str[:3]))
    second_half_sum = int(ticket_str[3]) + int(ticket_str[4]) + int(ticket_str[5]) # could used - sum(map(int, ticket_str[3:]))

    # Check if the sum of the first three digits is equal to the sum of the last three digits
    if first_half_sum == second_half_sum:
        return "Lucky"
    else:
        return "Unlucky"


# enter input data
ticket_number = input('введите число: ')
# ticket_number = random.randint(100000, 999999)


# ouput data rezult
print(f'this number {ticket_number} is {is_lucky(ticket_number)}')
  # Output: True
