teams = ["manchester united", "liverpool", "chelsea", "arsenal", "manchester city"]
print(teams[0])

print(teams[-3])

#eliminate element in list
print(teams[1:])
print(teams[1:3])

#add and remove element in list
teams.append("tottenham")
print(teams)

teams.remove("chelsea")
teams.insert(1, "chelsea")

#remove last element in list
teams.pop()
print(teams)    

#check elemnet in list
print(teams.count("chelseas"))