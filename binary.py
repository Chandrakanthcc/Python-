def binary_divisible_by_five(sequence):
    binary_numbers = sequence.split(',')
    divisible_by_five = []

    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            divisible_by_five.append(binary_number)

    return ','.join(divisible_by_five)

# Example usage:
if _name_ == "_main_":
    input_sequence = input("Enter a sequence of comma separated 4 digit binary numbers: ")
    result = binary_divisible_by_five(input_sequence)
    print("Numbers divisible by 5:", result)