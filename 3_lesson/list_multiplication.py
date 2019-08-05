def multiply_numbers(*numbers):
    mult = numbers[0]
    for number in numbers[1:]:
        mult = mult * number
    
    return mult

print(multiply_numbers(6, 5, 7, 3))
