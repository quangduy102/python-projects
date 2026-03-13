"""
This is a tutorial about how to handle exception in python
it help program run smoothly and constantly without crashing when an error occurs 
we use try and except block
"""
try:
    print(text)

except Exception as e:
    print("Exception: ", e)

# exception handle in calculator program
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))

try:
    print(f"Ket qua phep cong {num1} / {num2} = {num1 / num2}")
except ZeroDivisionError as e: 
    print("Khong the chia cho 0: ", e)