# Найдите сумму цифр трехзначного числа.
print('Task #2')

# -M- Method of calcualte of the number


def sum_of_digits(num_str):
    # Check that the input is a three-digit number
    if not num_str.isnumeric() or len(num_str) != 3:
        print("Error: Please enter a three-digit number.")
        return None
    # Calculate the sum of digits
    digits_sum = int(num_str[0]) + int(num_str[1]) + int(num_str[2])

    # Return the sum of digits
    return digits_sum


# enter input data
number = input('введите число: ')  # user given three-digit number

# ouput data rezult
result = sum_of_digits(number)
print(result)
