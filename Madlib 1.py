# This program is a Madlib, getting the user to enter details
# Then it prints out a story
print("Welcome to my Madlib program")
name = input("Name:")
subject = input("Enter a subject:")
illness = input("Enter and illness:")
body_part = input("Enter body part:")
number = input("Enter a number greater than 1")

print("Please excuse my son {} from {} today. He is suffering from a badcase of {} which has caused him a lot of {} pain. ".format(name, subject, illness, body_part))