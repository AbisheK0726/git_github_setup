# Get user input for there details
Fname = input("Please enter your first name: ")
Lname = input("Please enter your last name: ")
DOB = str(input("Please enter your year of birth: "))
House_number = str(input("Please enter your house number: "))
Address = input("Please enter your address: ")
Role = input("Please enter your role: ")
Salary = int(input("Please enter your salary: "))
Travel = float(input("Please enter your travel allowance: "))
Hobbies = input("Please enter ONE of your hobbies: ")

# Print the user details
print("\nYour name is", Fname, Lname)
print("Your DOB is", DOB)
print("Your address is", House_number, Address)
print("Your role is", Role, "and your salary is £{:,}".format(Salary), "and your travel allowance is £{:,}".format(Travel))
print("One of your hobbies is", Hobbies)