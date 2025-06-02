"""This is a module practice questions"""

__author__ = "Ivan Estropigan"
__version__ = "1.0"
__Credits__ = "COMP-1327, w3school"

pounds = 1
kg = 0.454

convert_kg_pounds = kg / pounds
convert_pounds_kg = pounds * kg
## Question 1  
print("*", "","","*","\n"
      "", "*", "*", "","\n"
      "", "", "*","\n"
      "", "*", "*", "","\n"
      "*", "","","*","\n")

## Question 2
print("Welcome to my program! This program will convert KG to Pounds")
convert_kg_pounds10 = (pounds / kg) * 10
convert_kg_pounds50 = (pounds / kg) * 50
convert_kg_pounds100 = (pounds / kg) * 100
print(f"10 KG is equal to: {convert_kg_pounds10:.2f} pounds")
print(f"50 KG is equal to: {convert_kg_pounds50:.2f} pounds")
print(f"100 KG is equal to: {convert_kg_pounds100:.2f} pounds")

## Question 3
weight = float(input("Choice [1] KG TO POUNDS | Choice [2] POUNDS TO KG "))

if weight == '1':
    weight = input(kg * pounds)
    print("Your weight is: {weight} pounds")
elif weight == '2':
    weight = pounds / kg
    print(f"Your weight is: {weight}")
else:
    print(f"{weight} is invalid")