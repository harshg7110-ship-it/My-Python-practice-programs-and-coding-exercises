# a='harsh'
# print ( a[-4:-2]) # ya to positve me convert karlo yafir left to right likh lo
# print(a[1:3])

# print(a[:4]) # agar 4 ke aage kuch nahi lika hai to 0 consider hoga  4 ki jaga koi bhi number ho sakta hai 
# print(a[1:]) # agar piche kuch nahi likha to name ka last number letter consider kiya jata hai jase yaha par 5 hoga


# Traditional Method:
name="Harsh"
age=19
print("My name is", name, "and my age is", age)
# Output:My name is Rahul and my age is 20

#Formatted string
#it is a special type of string in Python that allows us to insert variables or expressions directly inside a string.

#syntax =f"message {variable}" or F"message {variable}" 
 
first = "John"
last = "Smith"
print(f"My name is {first} {last}") # Output: My name is John Smith

#Replacement Field -> it is the part inside curly braces 
name = "Python"
print(f"I love {name}")
# Here:{name} is the replacement field.

a = 10
b = 20
print(f"Sum = {a+b}") # output = 30

# Format Specifier Concept.
# Syntax:{variable:format}

pi = 3.141592
print(f"{pi:.2f}") #output=3.14

# comma separator
salary = 1234567
print(f"{salary:,d}") #output=1,234,567

#Fixed decimal places
price = 99.56789
print(f"{price:.2f}") # Output:99.57



