def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number!")
else:
    print(number, "is not an Armstrong number.")
