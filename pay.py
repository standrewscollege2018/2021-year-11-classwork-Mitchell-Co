

age=int(input("What is your age:"))

if age < 5:
    print("Free")
elif age < 13:
    print("$7")
else:
    student = input("Are you a student? (yes/no)")
    if student == "yes":
        print("$8")
    elif age >= 18:
        print("$12")
    else:
        print("$9")