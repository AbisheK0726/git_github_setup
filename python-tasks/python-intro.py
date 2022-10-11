# Python is a dynamic language
# Python Variables?
# Variables are containers for storing data values
# To store user data - hard code the data - any other type
# first_name = "Abishek" - String
# last_name = "Aneese" - String
# DOB = 2001 - Int
# UK_resident = True - Boolean
# Salary = 40000 - Int
# Travel = 15.4 - Float

first_name = "Abishek"
last_name = "Aneese"
salary = 40000
travel = 15.4

#print()
print(first_name)
print(last_name)
print(salary)
print(travel)

# How to print the data type of a variable?
print(type(first_name)) # str
print(type(salary)) # int

#interact with the user by using the input() function

your_first_name = input("Please enter your first name: ")
your_last_name = input("Please enter your last name: ")
your_DOB = input("Please enter your date of birth: ")
your_course = input("Please enter your course: ")
your_uk_resident = input("Are you a UK resident? (True/False): ")

print(your_first_name, your_last_name, your_DOB, your_course, your_uk_resident)
