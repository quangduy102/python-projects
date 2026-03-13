# Branch Statement in Python

a = 50
b = 100

if a > b and a > 0: 
    print("a is greater than b")    
elif a < b or a < 0:
    print("a is less than b")
else:
    print("a is equal to b")    
#use not operator to negate the condition
if not a > b: #equaly to if a <=b 
    print("a is not greater than b")

#improve calculator program by using branch statement
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))

operator = input("Nhap phep toan (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2        
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Khong the chia cho 0"
else:
    result = "Phep toan khong hop le"   
print(f"Ket qua cua phep toan {num1} {operator} {num2} = {result}")