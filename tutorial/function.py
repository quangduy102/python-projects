#It's time to learn about function in python. Function is a block of code that performs a specific task

def greet(name):
    print(f"Hello {name}, welcome to python programming")

name = input("Please enter your name: ")
greet(name)

#return statement in function
def add(num1, num2):
    return num1 + num2

result = add(5, 10)
print(f"The result of addition is: {result}")

def check_element_in_list(element, list):
    return list.count(element) > 0

my_list = [1, 2, 3, 4, 5]
print(check_element_in_list(3, my_list))

#return multiple values in function
def calculate(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return sum, difference, product, quotient
result = calculate(10, 5)
print(result)

print(type(result))

#convert tuple to list
print(list(result))