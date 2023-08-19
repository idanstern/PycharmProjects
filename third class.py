try:
    a = 1 / 0

except ZeroDivisionError:
    print("Error: Division by zero!")

try:
    x = 1
finally:
    print("finally")
#the "" in print was not in python lang.

#4
#try:
    # Code that may raise exceptions
#except:
    # Exception handling code

#5:
#Difficulty in Debugging: When an exception occurs,
# it is helpful to know the specific type of exception that was raised

#6
try:
    # Code that may raise an input/output error
    file = open("file.txt", "r")
    # Additional code
except OSError:
    print("Input/Output error occurred.")
except FileNotFoundError:
    print("File not found.")

#7
my_name = open("words.txt")
words = my_name.readline()
print(words)