# Problem Statement:
# Create a salary calculator.
# Input:
# ● Employee name
# ● Basic salary
# ● Bonus
# ● Tax
# Calculate final salary.
# Formula:
# Final Salary = Basic Salary + Bonus - Tax


Name = input("Enter Employee Name:")
basic = int(input("Enter Basic Salary:"))
bonus = int(input("Enter bonus:"))
tax = int(input("Enter Tax:"))

final_salary = basic + bonus - tax
print("\nEmployee", Name, sep=": ")
print("Basic Salary", basic, sep=": ")
print("Bonus", bonus, sep=": ")
print("Tax", tax, sep=": ")
print("\nFinal Salary", final_salary, sep=": ")
