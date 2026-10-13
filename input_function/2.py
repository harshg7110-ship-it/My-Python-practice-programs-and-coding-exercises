# Problem Statement:
# Create a banking system that takes account holder name, initial balance, deposit amount, and
# withdrawal amount.
# Display final balance.


holder = input("Enter Account Holder Name:")
open = int(input("Enter Opening Balance:"))
deposite = int(input("Enter Deposite:"))
withdrawal = int(input("Enter Withdrawal:"))

final = open+deposite-withdrawal

print("="*10,"Bank Statement","="*10)

print("\nHolder:",holder)
print("Opening Balance:",open)
print("Deposite:",deposite)
print("Withdrawal:",withdrawal)
print("\nFinal Balance:",final)

print("="*36)