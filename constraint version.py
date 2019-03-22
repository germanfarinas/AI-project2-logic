from constraint import *

problem = Problem()


Color = ["Blue", "Green", "Lilac", "Pink", "Purple"]
Name = ["Georgina", "Hannah", "Jessica", "Jo", "Lucy"]
Chocolate = ["Boost", "Crunchies", "Dairy Milk", "Milky Bars", "Wispa Bites"]
Pet = ["Crocodile", "Hamster", "Horse", "Puppy", "Rabbit"]
Hobby = ["Horse riding", "Skiing", "Swimming", "Ten-pin bowlings","Tennis"]
Holiday = ["Australia", "Canada", "Florida", "Maldives", "Tobago"]

# add variables: house numbers 1 to 5

problem.addVariables(Color, range(1, 5 + 1))
problem.addVariables(Name, range(1, 5 + 1))
problem.addVariables(Chocolate, range(1, 5 + 1))
problem.addVariables(Pet, range(1, 5 + 1))
problem.addVariables(Hobby, range(1, 5 + 1))
problem.addVariables(Holiday, range(1, 5 + 1))

# add constraint: the values in each list are exclusive
problem.addConstraint(AllDifferentConstraint(), Color)
problem.addConstraint(AllDifferentConstraint(), Name)
problem.addConstraint(AllDifferentConstraint(), Chocolate)
problem.addConstraint(AllDifferentConstraint(), Pet)
problem.addConstraint(AllDifferentConstraint(), Hobby)
problem.addConstraint(AllDifferentConstraint(), Holiday)

# add constraint: actual constraints
problem.addConstraint(lambda a, b: a == b, ["Jo", "Wispa Bites"])
problem.addConstraint(lambda a, b: a == b, ["Hamster", "Swimming"])
problem.addConstraint(lambda a, b: a == b, ["Hannah", "Dairy Milk"])
problem.addConstraint(lambda a, b: a == b+1 or a == b+2 or a == b+3, ["Jessica", "Georgina"])
problem.addConstraint(lambda a: a == 1, ["Lucy"])
problem.addConstraint(lambda a: a == 5, ["Swimming"])
problem.addConstraint(lambda a, b: a == b, ["Milky Bars", "Horse"])
problem.addConstraint(lambda a: a == 3, ["Dairy Milk"])
problem.addConstraint(lambda a, b: a == b, ["Jessica", "Green"])
problem.addConstraint(lambda a: a == 2 or a == 1, ["Tobago"])
problem.addConstraint(lambda a, b: a == b, ["Maldives", "Lilac"])
problem.addConstraint(lambda a, b: a == b, ["Wispa Bites", "Florida"])
problem.addConstraint(lambda a, b: a == b, ["Pink", "Florida"])
problem.addConstraint(lambda a: a == 1, ["Lilac"])
problem.addConstraint(lambda a, b: a == b, ["Blue", "Puppy"])
problem.addConstraint(lambda a, b: a == b+1 or a == b-1, ["Skiing", "Hamster"])
problem.addConstraint(lambda a, b: a == b+1 or a == b+2 or a == b+3 or a == b+4, ["Tennis", "Horse riding"])
problem.addConstraint(lambda a, b: a == b+1 or a == b-1, ["Milky Bars", "Boost"])
problem.addConstraint(lambda a, b: a == b, ["Crunchies", "Rabbit"])
problem.addConstraint(lambda a, b: a == b+1 or a == b-1, ["Skiing", "Ten-pin bowlings"])
problem.addConstraint(lambda a, b: a == b, ["Jessica", "Australia"])





# get solution
sol = problem.getSolution()

# print the answers
color = ["Color" if i == 0 else "" for i in range(6)]
name = ["Name" if i == 0 else "" for i in range(6)]
chocolate = ["Chocolate" if i == 0 else "" for i in range(6)]
pet = ["Pet" if i == 0 else "" for i in range(6)]
hobby = ["Hobby"if i == 0 else "" for i in range(6) ]
holiday = ["Holiday" if i == 0 else "" for i in range(6)]
for n in Color:
    color[sol[n]] = n
for n in Name:
    name[sol[n]] = n
for n in Chocolate:
    chocolate[sol[n]] = n
for n in Pet:
    pet[sol[n]] = n
for n in Hobby:
    hobby[sol[n]] = n
for n in Holiday :
    holiday[sol[n]] = n
for d in [color, name, chocolate, pet, hobby,holiday]:
    print("%-10s: %-20s%-20s%-20s%-20s%-20s" % (d[0], d[1], d[2], d[3], d[4], d[5]))

