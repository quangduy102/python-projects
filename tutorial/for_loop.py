#for loop in Python

for i in range(1, 10):
    print(i)

#for with list
teams = ["manchester united", "liverpool", "chelsea", "arsenal"]
for team in teams:
    print(team)

for i in range(1,11):
    print(f"{i} x {i} = {i*i}")
#exponential:

def exponential(base, exp):
    return base ** exp
print(exponential(2, 3))