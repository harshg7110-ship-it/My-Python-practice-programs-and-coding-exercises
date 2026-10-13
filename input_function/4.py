# Problem Statement:
# Create a program that takes units consumed and cost per unit as input and calculates the
# electricity bill.
# Formula:
# Bill = Units × Cost per Unit


customer =(input("Enter Customer Name:"))
units = int(input("Enter Units:"))
rate = int(input("Enter Rate:"))

total= units*rate
print("\nCustomer Name:",customer)
print("Units:",units)
print("Rate:",rate)
print("\nTotal Bill:",total)
