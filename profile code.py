first_name = input("What is your first name: ")
surname = input("What is your surname: ")
current_year = int(input("What is the current year: "))
birth_year = int(input("What is your birth year: "))
age = birth_year - current_year
print(f"Welcome,{first_name} {surname}\n  b You are {age} years old")