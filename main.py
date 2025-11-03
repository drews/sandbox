# main.py - used to demo for learn-to-code

def greet(greetee, greeting = "👋 hello"):
    print(greeting + " " + greetee + " 🌟")

def sum(a, b) -> int:
    return a + b

# output to the console
greet("world🌎")

# # get input from the console
# name = input("what should I call you: ")
# greet(name, greeting="😊 hi there, ")

# total = sum(5, 7)
# print("the sum of 5 and 7 is: " + str(total) + " 🎉")

x = 15
if x > 10:
    print("Big number!")
elif x > 5:
    print("Medium number!")
else:
    print("Small number!")
