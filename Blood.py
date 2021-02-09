# This program will determine whether or not you are eligble for blood donating
AGE=16
WEIGHT=50

age = int(input("What is your age?"))
weight= int(input("What is your weight?"))

if age >= AGE and weight >= WEIGHT:
    print("You are eligible")

else:
    print("Not eligible")
