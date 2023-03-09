first_name = "Nii Narku"
last_name = "Noi"
phone_number = 269134014
age = 21

#How to create a list of multiple elements.
names_of_students = ["nii narku noi","gyamfi michael","asare kofi obeng"]

#List index starts from 0. So (0,1,2,3...).
#Selecting the second student on the list and assigning a variable "second_student" to it.
second_student = names_of_students[1]
print(second_student)

#Adding a new student to the list of students at the end. Use .append
names_of_students.append("newman")
print(names_of_students)

#Creating a list of 5 students, print, adding anmother student, and select a third student
#saving it in a variable called [third_student], remove the last student and print

names_of_students = ["Narku","Asare","Michael","Phinehas","Desmond"]
print(names_of_students)
names_of_students.push("Kenneth")
print(names_of_students)
third_student = names_of_students[2]
print(third_student)

#removing last element. Use ".pop"
names_of_students.pop[4]

#Python dictonary
my_details = {"name":"Nii","age":15, "gender":"Male"}

joels_info = {"name":"joel",
                "age":13,
                "hobbies": {"outdoor":["Roaming","ampe"],"indoor":["ludu","table_tennis"]}
                }
hobbies=joels_info["hobbies"]
outdoor= hobbies["outdoor"]
second_outdoor_hobby = outdoor[1]
print(second_outdoor_hobby)

#Grading students
students_grade = {}

#addong to the dictionary
students_grade["Mike"] = "A"
print(students_grade)
students_grade["Aaron"] = "B"
print(students_grade)
students_grade["Nii"] = "C"
print(students_grade)

#reomoving from the dictionary
students_grade.pop("Aaron")
