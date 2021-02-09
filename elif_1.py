#This program will take a score out of 100 and give an overall grade on an exam
#Variable that asks for score

score = int(input("What was your final score: "))

#Calculates score determined by number
if score>=0 and score<=100:

    if score is 100 :
        print("Congrats you've recieved an A on your exam!")

    elif score is 90 :

        print("You've recieved a B on your exam")

    elif score is 50 :
        print("You've recieved a C on your exam")

    else:
        print("Damn you failed")
else:
    print('Invalid mark')
