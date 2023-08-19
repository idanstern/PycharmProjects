#1
import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

angle_radians = 1.5
angle_degrees = radians_to_degrees(angle_radians)
print(angle_degrees)

#2
def sort_numbers(numbers, order):
    if order == "asc":
        return sorted(numbers)
    elif order == "desc":
        return sorted(numbers, reverse=True)
    elif order == "none":
        return numbers
    else:
        raise ValueError("Invalid sorting order. Please choose 'asc', 'desc', or 'none'.")

numbers = [5, 2, 8, 1, 9]
order = "asc"
sorted_numbers = sort_numbers(numbers, order)
print(sorted_numbers)

#3
def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'

    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary
decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")

#4
