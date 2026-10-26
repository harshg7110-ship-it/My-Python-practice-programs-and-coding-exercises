# A function argument is a value that we give to a function when we call the function.
from functools import reduce


def greet(name):
  print("Hello", name) # name is parameter and Harsh is argument
greet("Harsh")

#def → keyword used to create a function.
#student → function name.
#name and age → parameters.

def student(name, age):
    print(name)
    print(age)
student("Aman", 20)

#Normal function
def square(x):
    return x * x
print(square(5))

# Lambda function: small anonymous function
multiply = lambda a, b: a * b  # a aur b input hain, unka multiplication return hoga
print(multiply(4, 5))  # Function call: a = 4, b = 5, output = 20

add = lambda a, b: a + b
print(add(10, 20))

sub = lambda a,b: a-b
print(sub(30,2))

maximum = lambda a, b: a if a > b else b # Agar a > b hai toh a return hoga, warna b return hoga
print(maximum(8, 12)) # Function call: a = 8, b = 12, output = 12

#map() in lambda function
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result)) #Here, map() applies x * 2 to every element of the list.

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x ** 2 if x % 2 == 0 else x, numbers)
print(list(result))

# filter() with lambda function
numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, numbers)  # Sirf even numbers ko filter karega
print(list(even))  #output = [2, 4, 6]

#reduce() with lambda function
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)  # Do numbers ko add karke ek final result dega
print(result)  # Final sum print karega

# Output:10
# initially =[1, 2, 3, 4]
# First: x = 1, y = 2,  1 + 2 = 3
# Now[3, 3, 4]
# Next: ,x = 3 ,y = 3 ,3 + 3 = 6
# Now:[6, 4]
# Finally:6 + 4 = 10


