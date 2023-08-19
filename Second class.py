#A:
X = 10
Y = 5

if X > Y:
    print("BIG")
elif X < Y:
    print("small")

#B:
for i in range(1, 6):
    print(i)

#C
def season():
    season1 = int(input("what season we are now? "))

    if season1 == 1:
        print("summer")
    elif season1 == 2:
        print("winter")
    elif season1 == 3:
        print("fall")
    elif season1 == 4:
        print("spring")
    else:
        print("Invalid")
season()

#D
count = 1
while count < 11:
    print(count)
    count = count + 1

#E
age = 33
letter = "S"
currency = 3.52
flew = True
apartment_number = 20

print(age)
print(letter)
print(currency)
print(flew)
print(apartment_number)
print(currency+age)

#F
number = input("Enter your phone number: ")
print("Phone number", number)

#G
def printHello():
    print("hello")

def calculate():
    print(5+3.2)

#H
def print_name(name):
    print(name)

def divide_number(num):
    print(num/2)

#I
def return_sum(x,y):
    return x+y

def add_space(word_a, word_b):
    return word_a + " " + word_b

# Challenge K
stars = 5
for i in range(stars):
    print("*" *(i + 1))

# Challenge L
stars = 7
lines = 7

for i in range(lines):
    for j in range(stars):
        if i == j or i == (stars - j - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Challenge M
def phone():
    number = input("Enter a number: ")
    return int(number)

def sum(number):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits

number = phone()
digit_sum = sum(number)
print("The sum of the digits in the number is:", digit_sum)
