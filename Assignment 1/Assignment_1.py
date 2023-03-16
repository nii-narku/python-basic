"""
Write a python scriot that takes input from a user and display it to the
user in a well formatted output. (Use the concept of list)
details:
Name, Age, Class, Gender
"""

user_details = []
user_input = input("Enter your name:\n")
user_details.append(user_input)
user_input = input("Enter your age:\n")
user_details.append(user_input)
user_input = input("Enter your class:\n")
user_details.append(user_input)
user_input = input("Enter your gender:\n")
user_details.append(user_input)
user_input = input("Enter telephone number:\n")
user_details.append(user_input)

print(f"Your name is {user_details[0]}. Your age is {user_details[1]}. Your class is {user_details[2]}. Your gender is {user_details[3]}. Your telephone number is {user_details[4]}")
