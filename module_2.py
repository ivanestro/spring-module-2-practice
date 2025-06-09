"""This is a module practice questions"""

__author__ = "Ivan Estropigan"
__version__ = "1.0"
__Credits__ = "COMP-1327, w3school"

pounds = 1
kg = 0.454
millimeters = 1 * 25.4
circumference = 2 * 3.14 * 3.2

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


if weight == 1:
    weight = input("Type the weight in Kilogram ")
    convert_kg_pounds = float(weight) * pounds / kg
    print(f"Your weight is: {convert_kg_pounds:.2f} pounds")
elif weight == 2:
    weight = input("Type the weight in Pounds ")
    convert_pounds_kg = float(weight) * kg / pounds
    print(f"Your weight is: {convert_pounds_kg:.2f} KG")
else:
    print(f"{weight} is invalid")

# Question 4 
print("\nWelcome this is to convert inches to millimeters")
print(f"2 inches is equal to: {2 * millimeters} millimeters" )
print(f"5 inches is equal to: {5 * millimeters} millimeters")
print(f"10 inches is equal to {10 * millimeters} millimeters")
""" This program converts 2, 5, and 10 inches to millimeters (1 inch = 25.4 mm).

args: 
millimeters = 1 * 25.4

Return:
2 inches is equal to: 50.8 millimeters
5 inches is equal to: 127.0 millimeters
10 inches is equal to 254.0 millimeters
"""

# Question 5 
convert = float(input("\nChoice [1] Inches to Milli | Choice [2] Lengths in Inches "))

if convert == 1:
    convert = input("Type the inches you want to convert? ")
    convert_milli = float(convert) * millimeters
    print(f"Your conversion is: {convert_milli} millimeter")
elif convert == 2:
    convert = input("Type the inches you want to convert to length? ")
    convert_length = float(convert) * 2.54
    print(f"Your length is {convert_length}")
else: 
    print("You have input the wrong value ")
"""Question 5: Update the previous program to accept the lengths in inches from the user. 

args:
convert_milli = float(convert) * millimeters
convert_length = float(convert) * 2.54

result: 
Choice [1] Inches to Milli | Choice [2] Lengths in Inches 1
Type the inches you want to convert? 1
Your conversion is: 25.4 millimeter

Choice [1] Inches to Milli | Choice [2] Lengths in Inches 2
Type the inches you want to convert to length? 1
Your length is 2.54
"""

# Question 6 
print(f"\nThis program will compute circumference")
print(f"The circumference is: {circumference:.2f} circumference")
"""Question 6: Write a program to compute and output the 
circumference of a circle having a radius of 3.2 inches


args:
circumference = 2 * 3.14 * 3.2

result:
This program will compute circumference
The circumference is: 20.10 circumference
"""

# Update Question 6
"""Updated Question 6: 
Update the previous program to accept the radius from the user. 
Use the entered value to calculate and output the circle's circumference and area.

A: The area of the circle.
r: The radius of the circle.
"""
print(f"\nWelcome to Circumference Calculator")

choice = float(input("Choice [1] Circumference | Choice [2] Radius | Choice [3] Circumference and Area "))
if choice == 1:
    circumference = float(input("Calculate your Circumference? "))
    circumference = float(circumference) * (3.14 * 2)
    print(f"Your circumference is: {circumference}")

elif choice == 2:
    circumference = input("What is your circumference ")
    answer = float(circumference) / (2 * 3.14)
    print(f"Your Radius is {answer:.2f}")

elif choice == 3:
    circumference = input("What is your circumference? ")
    circumference = float(circumference) / 2 * 3.14
    radius = input("What is your Radius? ")
    radius = 3.14 * float(radius) * 2
    print(f"Your circumference is {circumference}, Your Area is {radius}")
else:  
    print("invalid")


# Question 8 
print("\nWelcome to Comparing two words that are shorter.")

word = input("Please write a word: ")
word2 = input("Write another word: ")

if word > word2: 
    print(f"Your first word is shorter than word 2.{len(word)} The words are {word}, {word2}")

elif word2 > word:
    print(f"The length of your second word is: {len(word2)} The words are {word}, {word2}")

