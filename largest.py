def largest_even_odd(numbers):
    largest_even = None
    largest_odd = None
    
    for num in numbers:
        if num % 2 == 0:  
            if largest_even is None or num > largest_even:
                largest_even = num
        else:  
            if largest_odd is None or num > largest_odd:
                largest_odd = num
                
    return largest_even, largest_odd

numbers = [1, 4, 7, 2, 9, 6, 5, 8]
largest_even, largest_odd = largest_even_odd(numbers)
print("Largest even number:", largest_even)
print("Largest odd number:", largest_odd)
