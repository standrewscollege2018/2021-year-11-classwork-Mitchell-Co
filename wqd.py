

keep = True

while keep == True:
    try:
        number = int(input("Enter integer"))
        print("You choose", number)
        keep = False
    except:
        print("That's not an integer")
print("********")

