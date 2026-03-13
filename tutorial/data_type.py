
import math
chanel_name = "duytq"

print(f"This is my chanel {chanel_name} and {len(chanel_name)}")

# number data type
number = 2
print(f"{number}")

#convert nunber to stirng 

number_str = str(number)
print(f"{number_str} and {type(number_str)}")

#convert string to number
number_float = float(number_str)
print(f"{number_float} and {type(number_float)}")

#max
print(max(3,4,6))

#floor and ceil
print(math.floor(3.7))
print (math.ceil(3.7))

name = input("Nhap ten cua ban vao day: ")
age = input("Nhap tuoi cua ban vao day: ")

print(f"Xin chao {name}, ban da {age} tuoi roi do")